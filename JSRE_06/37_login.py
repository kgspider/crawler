#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random

import execjs
import requests


login_url = 'https://my.37.com/api/login.php'


def get_encrypted_password(password):
    with open('37_encrypt.js', 'r', encoding='utf-8') as f:
        www_37_js = f.read()
    encrypted_pwd = execjs.compile(www_37_js).call('getEncryptedPassword', password)
    return encrypted_pwd


def login(username, encrypted_password):
    timestamp = str(int(time.time() * 1000))
    jsonp = ''
    for _ in range(20):
        jsonp += str(random.randint(0, 9))
    callback = 'jQuery' + jsonp + '_' + timestamp
    params = {
        'callback': callback,
        'action': 'login',
        'login_account': username,
        'password': encrypted_password,
        'ajax': 0,
        'remember_me': 1,
        'save_state': 1,
        'ltype': 1,
        'tj_from': 100,
        's': 1,
        'tj_way': 1,
        '_': timestamp
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"'
    }
    response = requests.post(url=login_url, headers=headers, params=params)
    print(response.text)


def main():
    username = input('请输入登录账号: ')
    password = input('请输入登录密码: ')
    encrypted_password = get_encrypted_password(password)
    login(username, encrypted_password)


if __name__ == '__main__':
    main()
