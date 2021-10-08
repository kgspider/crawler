#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re

import execjs
import requests


index_url = 'http://zwfw.san-he.gov.cn/icity/icity/guestbook/interact'
data_url = 'http://zwfw.san-he.gov.cn/icity/api-v2/app.icity.guestbook.WriteCmd/getList'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
session = requests.session()


def get_encrypted_parameters(signature):
    with open('zwfw_san_he_encrypt.js', 'r', encoding='utf-8') as f:
        zwfw_san_he_js = f.read()
    encrypted_parameters = execjs.compile(zwfw_san_he_js).call('getDecryptedParameters', signature)
    return encrypted_parameters


def get_signature_and_cookies():
    response = session.get(url=index_url, headers=headers)
    cookies = response.cookies.get_dict()
    cookie = cookies['ICITYSession']
    signature = re.findall(r'signature = "(.*)"', response.text)[0]
    return cookie, signature


def get_data(cookie, parameters, page):
    payload_data = {'start': page*7, 'limit': 7, 'TYPE@=': '2', 'OPEN@=': '1'}
    params = {'s': parameters['s'], 't': parameters['t']}
    cookies = {'ICITYSession': cookie}
    response = session.post(url=data_url, headers=headers, json=payload_data, params=params, cookies=cookies).json()
    print(payload_data, response)


def main():
    ck, sig = get_signature_and_cookies()
    for page in range(10):
        # 采集10页数据
        param = get_encrypted_parameters(sig)
        get_data(ck, param, page)


if __name__ == '__main__':
    main()
