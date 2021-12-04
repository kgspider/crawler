# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-11-10
# @Author  : 微信公众号：K哥爬虫
# @FileName: open_login.py
# @Software: PyCharm
# ==================================


import time
import execjs
import requests


login_url = "https://learn.open.com.cn/Account/UnitLogin"


def get_black_box():
    with open('get_black_box.js', 'r', encoding='utf-8') as f:
        exec_js = f.read()
    black_box = execjs.compile(exec_js).call('OOoO0')
    return black_box


def login(black_box, username, password):
    params = {"bust": str(int(time.time() * 1000))}
    data = {
        "loginName": username,
        "passWord": password,
        "validateNum": "",
        "black_box": black_box
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }
    response = requests.post(url=login_url, params=params, data=data, headers=headers)
    print(response.json())


def main():
    username = input("请输入登录账号: ")
    password = input("请输入登录密码: ")
    black_box = get_black_box()
    login(black_box, username, password)


if __name__ == '__main__':
    main()
