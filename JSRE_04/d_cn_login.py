#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import execjs
import requests


def get_encrypted_password(password):
    with open('d_cn_encrypt.js', 'r', encoding='utf-8') as f:
        weibo_js = f.read()
    encrypted_password = execjs.compile(weibo_js).call('getEncryptedPassword', password)
    return encrypted_password


def login(encrypted_password, username):
    login_url = 'https://oauth.d.cn/auth/login'
    headers = {
        'Host': 'oauth.d.cn',
        'Referer': 'https://oauth.d.cn/auth/goLogin.html',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    params = {
        'display': 'web',
        'name': username,
        'pwd': encrypted_password,
        'to': 'https%3A%2F%2Fwww.d.cn%2F'
    }
    response = requests.get(url=login_url, params=params, headers=headers).json()
    print(response)


def main():
    username = input('请输入登录账号: ')
    password = input('请输入登录密码: ')
    encrypted_password = get_encrypted_password(password)
    login(encrypted_password, username)


if __name__ == '__main__':
    main()
