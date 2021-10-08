#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import hashlib

import execjs
import requests


login_url = 'https://gateway.ewt360.com/api/authcenter/v2/oauth/login/account'
session = requests.session()


def get_sign():
    timestamp = str(int(time.time()*1000))
    sign = hashlib.md5((timestamp + 'bdc739ff2dcf').encode(encoding='utf-8')).hexdigest().upper()
    return sign


def get_encrypted_parameter(password):
    with open('ewt360_encrypt.js', 'r', encoding='utf-8') as f:
        ewt360_js = f.read()
    encrypted_password = execjs.compile(ewt360_js).call('getEncryptedPassword', password)
    return encrypted_password


def login(sign, username, encrypted_password):
    headers = {
        'sign': sign,
        'timestamp': str(int(time.time()*1000)),
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    data = {
        'autoLogin': True,
        'password': encrypted_password,
        'platform': 1,
        'userName': username
    }
    response = session.post(url=login_url, headers=headers, json=data)
    print(response.json())


def main():
    username = input('请输入登录账号: ')
    password = input('请输入登录密码: ')
    sign = get_sign()
    encrypted_password = get_encrypted_parameter(password)
    login(sign, username, encrypted_password)


if __name__ == '__main__':
    main()
