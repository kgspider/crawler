#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json

import execjs
import requests


data_url = 'http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list?pg=%s&pgsz=15&total=450'


def get_encrypted_data(page):
    headers = {
        'Host': 'jzsc.mohurd.gov.cn',
        'Referer': 'http://jzsc.mohurd.gov.cn/data/company',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    encrypted_data = requests.get(url=data_url % page, headers=headers).text
    return encrypted_data


def get_decrypted_data(encrypted_data):
    with open('jzsc_mohurd_decrypt.js', 'r', encoding='utf-8') as f:
        jzsc_mohurd_js = f.read()
    decrypted_data = execjs.compile(jzsc_mohurd_js).call('getDecryptedData', encrypted_data)
    return json.loads(decrypted_data)


def main():
    # 30页数据
    for page in range(30):
        encrypted_data = get_encrypted_data(page)
        decrypted_data = get_decrypted_data(encrypted_data)
        print(decrypted_data)


if __name__ == '__main__':
    main()
