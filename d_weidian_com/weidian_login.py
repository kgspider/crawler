# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-11-15
# @Author  : 微信公众号：K哥爬虫
# @FileName: weidian_login.py
# @Software: PyCharm
# ==================================


import execjs
import requests
from urllib import parse


index_url = "https://d.weidian.com/weidian-pc/pc-vue-index/index.html"
login_url = "https://sso1.weidian.com/user/login"
UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
session = requests.session()


def get_encrypted_ua():
    with open('get_encrypted_ua.js', 'r', encoding='utf-8') as f:
        uad_js = f.read()
    ua = execjs.compile(uad_js).call('window.getUa')
    ua = parse.quote(ua)
    return ua


def get_wd_token():
    headers = {"User-Agent": UserAgent}
    response = session.get(url=index_url, headers=headers)
    wd_token = response.cookies.get_dict()["wdtoken"]
    return wd_token


def login(phone, password, ua, wd_token):
    headers = {
        "user-agent": UserAgent,
        "origin": "https://d.weidian.com",
        "referer": "https://d.weidian.com/",
    }
    data = {
        "phone": phone,
        "countryCode": "86",
        "password": password,
        "version": "1",
        "subaccountId": "",
        "clientInfo": '{"clientType": 1}',
        "captcha_session": "",
        "captcha_answer": "",
        "vcode": "",
        "mediaVcode": "",
        "ua": ua,
        "scene": "PCLogin",
        "wdtoken": wd_token
    }
    response = session.post(url=login_url, headers=headers, data=data)
    print(response.json())


def main():
    phone = input("请输入登录手机号: ")
    password = input("请输入登录密码: ")
    ua = get_encrypted_ua()
    wd_token = get_wd_token()
    login(phone, password, ua, wd_token)


if __name__ == '__main__':
    main()
