#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re

import execjs
import requests


index_url = 'https://passport.fang.com/'
login_url = 'https://passport.fang.com/login.api'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
session = requests.session()


def get_key_to_encode():
    headers = {'User-Agent': user_agent}
    response = session.get(url=index_url, headers=headers)
    key_to_encode = re.findall(r'RSAKeyPair\((.*)\);', response.text)[0].replace('"', '').split(', ')
    return key_to_encode


def get_encrypted_password(key_to_encode, pwd):
    n, i, t = key_to_encode[0], key_to_encode[1], key_to_encode[2]
    with open('fang_encrypt.js', 'r', encoding='utf-8') as f:
        fang_js = f.read()
    encrypted_pwd = execjs.compile(fang_js).call('getEncryptedPassword', pwd, n, i, t)
    return encrypted_pwd


def login(encrypted_password, uid):
    headers = {
        'User-Agent': user_agent,
        'X-Requested-With': 'XMLHttpRequest',
        'Host': 'passport.fang.com',
        'Origin': 'https://passport.fang.com',
        'Referer': 'https://passport.fang.com/?backurl=http%3a%2f%2fmy.fang.com%2f',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    data = {
        'uid': uid,
        'pwd': encrypted_password,
        'Service': 'soufun-passport-web',
        'AutoLogin': 1
    }
    response = session.post(url=login_url, data=data, headers=headers)
    print(response.json())


def main():
    # 16521689404
    uid = input('请输入登录账号：')
    pwd = input('请输入登录密码：')
    rsa_key = get_key_to_encode()
    encrypted_pwd = get_encrypted_password(rsa_key, pwd)
    login(encrypted_pwd, uid)


if __name__ == '__main__':
    main()
