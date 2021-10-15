# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-10-12
# @Author  : 微信公众号：K哥爬虫
# @FileName: wcbchina_login.py
# @Software: PyCharm
# ==================================


import time
import random
import hashlib

import execjs
import requests


login_url = 'https://m.wcbchina.com/api/login/login'


def get_enpwd_and_sign_by_javascript(password):
    with open('wcbchina_encrypt.js', 'r', encoding='utf-8') as f:
        encrypt_js = execjs.compile(f.read())
    encrypted_password = encrypt_js.call('getEncryptedPassword', password)
    sign = encrypt_js.call('getSign')
    return encrypted_password, sign


def get_enpwd_and_sign_by_python(password):
    timestamp = str(int(time.time() * 1000))
    encrypted_password = hashlib.md5(password.encode('utf-8')).hexdigest().upper()
    sign = hashlib.md5(timestamp.encode('utf-8')).hexdigest().upper()
    return encrypted_password, sign


def get_rnd():
    rnd = 'rnd' + str(random.uniform(0, 1))
    return rnd


def login(username, encrypted_password, sign, rnd):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    json = {
        "auth": {
            "timestamp": str(int(time.time() * 1000)),
            "sign": sign
        },
        "username": username,
        "password": encrypted_password
    }
    response = requests.post(url=login_url, params=rnd, json=json, headers=headers)
    print(response.json())


def main():
    username = input('请输入登录账号: ')
    password = input('请输入登录密码: ')
    # 通过 JavaScript 代码获取加密后的密码和 sign
    encrypted_password, sign = get_enpwd_and_sign_by_javascript(password)
    # 通过 Python 代码获取加密后的密码和 sign
    # encrypted_password, sign = get_enpwd_and_sign_by_python(password)
    rnd = get_rnd()
    login(username, encrypted_password, sign, rnd)


if __name__ == '__main__':
    main()
