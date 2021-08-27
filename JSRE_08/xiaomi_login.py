#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import hashlib
import urllib.parse

import requests


index_url = 'https://account.xiaomi.com/'
login_url = 'https://account.xiaomi.com/pass/serviceLoginAuth2'
headers = {
    'Host': 'account.xiaomi.com',
    'Origin': 'https://account.xiaomi.com',
    'Referer': 'https://account.xiaomi.com/fe/service/login/password?_locale=zh_CN',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
session = requests.session()


def get_encrypted_password(password):
    encrypted_password = hashlib.md5(password.encode(encoding='utf-8')).hexdigest().upper()
    return encrypted_password


def get_parameter():
    response = requests.get(url=index_url, headers=headers)
    location_url = response.history[1].headers['Location']
    urlparse = urllib.parse.urlparse(location_url)
    query_dict = urllib.parse.parse_qs(urlparse.query)
    # print(query_dict)
    return query_dict


def login(username, encrypted_password, query_dict):
    data = {
        'bizDeviceType': '',
        'needTheme': query_dict['needTheme'][0],
        'theme': '',
        'showActiveX': query_dict['showActiveX'][0],
        'serviceParam': query_dict['serviceParam'][0],
        'callback': query_dict['callback'][0],
        'qs': query_dict['qs'][0],
        'sid': query_dict['sid'][0],
        '_sign': query_dict['_sign'][0],
        'user': username,
        'cc': '+86',
        'hash': encrypted_password,
        '_json': True
    }
    response = session.post(url=login_url, data=data, headers=headers)
    response_json = json.loads(response.text.replace('&&&START&&&', ''))
    print(response_json)
    return response_json


def main():
    username = input('请输入登录账号: ')
    password = input('请输入登录密码: ')
    encrypted_password = get_encrypted_password(password)
    parameter = get_parameter()
    login(username, encrypted_password, parameter)


if __name__ == '__main__':
    main()
