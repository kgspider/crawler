# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-11-29
# @Author  : 微信公众号：K哥爬虫
# @FileName: zhihuishu_login.py
# @Software: PyCharm
# ==================================


import time
import json
import base64
import _thread
import requests
import websocket
from PIL import Image


web_socket_url = "wss://appcomm-user.zhihuishu.com/app-commserv-user/websocket?qrToken=%s"
get_login_qr_img_url = "https://passport.zhihuishu.com/qrCodeLogin/getLoginQrImg"
login_url = "https://passport.zhihuishu.com/login"
user_info_url = "https://onlineservice.zhihuishu.com/login/getLoginUserInfo"

headers = {
    "Host": "passport.zhihuishu.com",
    "Pragma": "no-cache",
    "Referer": "https://passport.zhihuishu.com/login",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

qr_token = ""
once_password = ""
uuid = ""
cookie = {}


def get_cookies_first():
    response = requests.get(url=login_url, headers=headers)
    global cookie
    cookie = response.cookies.get_dict()


def get_login_qr_img():
    response = requests.get(url=get_login_qr_img_url, headers=headers, cookies=cookie).json()
    qr_img = response["img"]
    global qr_token
    qr_token = response["qrToken"]
    with open('code.png', 'wb') as f:
        f.write(base64.b64decode(qr_img))
    image = Image.open('code.png')
    image.show()
    print("请扫描验证码! ")


def wss_on_message(ws, message):
    print("=============== [message] ===============")
    message = json.loads(message)
    print(message)
    if "扫码成功" in message["msg"]:
        global once_password, uuid
        once_password = message["oncePassword"]
        uuid = message["uuid"]
        ws.close()


def wss_on_error(ws, error):
    print("=============== [error] ===============")
    print(error)
    ws.close()


def wss_on_close(ws, close_status_code, close_msg):
    print("=============== [closed] ===============")
    print(close_status_code)
    print(close_msg)


def wss_on_open(ws):
    def run(*args):
        while True:
            ws.send(qr_token)
            time.sleep(8)
    _thread.start_new_thread(run, (qr_token,))


def wss():
    # websocket.enableTrace(True)  # 是否显示连接详细信息
    ws = websocket.WebSocketApp(
        web_socket_url % qr_token, on_open=wss_on_open,
        on_message=wss_on_message, on_error=wss_on_error,
        on_close=wss_on_close
    )
    ws.run_forever()


def get_cookie_second():
    global cookie
    params = {
        "pwd": once_password,
        "service": "https://onlineservice.zhihuishu.com/login/gologin"
    }
    headers["Host"] = "passport.zhihuishu.com"
    headers["Referer"] = "https://passport.zhihuishu.com/login"
    response = requests.get(url=login_url, params=params, headers=headers, cookies=cookie, allow_redirects=False)
    cookie.update(response.cookies.get_dict())
    location = response.headers.get("Location")
    return location


def get_cookie_third(location):
    global cookie
    headers["Host"] = "onlineservice.zhihuishu.com"
    headers["Referer"] = "https://passport.zhihuishu.com/"
    response = requests.get(url=location, headers=headers, cookies=cookie, allow_redirects=False)
    cookie.update(response.cookies.get_dict())
    location = response.headers.get("Location")
    return location


def get_login_user_info():
    headers["Host"] = "onlineservice.zhihuishu.com"
    headers["Origin"] = "https://onlineweb.zhihuishu.com"
    headers["Referer"] = "https://onlineweb.zhihuishu.com/"
    params = {"time": str(int(time.time() * 1000))}
    response = requests.get(url=user_info_url, headers=headers, cookies=cookie, params=params)
    print(response.text)


def main():
    # 第一次获取 cookie，包含 INGRESSCOOKIE、JSESSIONID、SERVERID、acw_tc
    get_cookies_first()
    # 获取二维码
    get_login_qr_img()
    # websocket 扫码登录，返回一次性密码
    wss()
    # 第二次获取 cookie，更新 SERVERID、获取 CASLOGC、CASTGC
    location1 = get_cookie_second()
    # 第三次获取 cookie，获取 SESSION
    get_cookie_third(location1)
    # 获取登录用户信息
    get_login_user_info()


if __name__ == '__main__':
    main()
