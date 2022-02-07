# ==================================
# @Time    : 2022-01-11
# @Author  : 微信公众号：K哥爬虫
# @FileName: hnzww_login.py
# @Software: PyCharm
# ==================================


import execjs
import requests


cookies = {}
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"

with open("encrypt.js", encoding="utf-8") as f:
    js = execjs.compile(f.read())


def csrf_save():
    url = "https://login.hnzwfw.gov.cn/tacs-uc/naturalMan/csrfSave"
    headers = {"User-Agent": UA}
    response = requests.post(url=url, headers=headers, cookies=cookies).json()
    data = response["data"]
    return data


def get_session():
    url = "https://login.hnzwfw.gov.cn/tacs-uc/login/index"
    headers = {"User-Agent": UA}
    response = requests.get(url=url, headers=headers)
    cookies.update(response.cookies.get_dict())


def get_uuid():
    url = "https://login.hnzwfw.gov.cn/tacs-uc/naturalMan/uploadIdentifier"
    headers = {
        "User-Agent": UA,
        "token": js.call("encrypt", csrf_save())
    }
    response = requests.post(url=url, headers=headers, cookies=cookies).json()
    uuid = response["data"]
    return uuid


def ver_code():
    url = "https://login.hnzwfw.gov.cn/tacs-uc/login/verCode"
    headers = {
        "User-Agent": UA,
        "token": js.call("encrypt", csrf_save())
    }
    response = requests.post(url=url, headers=headers, cookies=cookies).json()
    data = response["data"]
    return data


def login(phone, pwd, code, uuid):
    url = "https://login.hnzwfw.gov.cn/tacs-uc/naturalMan/loginNo"
    headers = {
        "User-Agent": UA,
        "token": js.call("encrypt", csrf_save())
    }
    data = {
        "backUrl": "",
        "loginNo": js.call("encrypt", phone),
        "loginPwd": js.call("encrypt", pwd),
        "code": code,
        "requestUUID": uuid,
        "guoBanAuthCode": ""
    }
    response = requests.post(url=url, headers=headers, cookies=cookies, data=data)
    print(response.json())


def main():
    phone = input("请输入账号：")
    pwd = input("请输入密码：")
    get_session()
    uuid = get_uuid()
    code = ver_code()
    login(phone, pwd, code, uuid)


if __name__ == '__main__':
    main()
