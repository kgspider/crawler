# =======================
# --*-- coding: utf-8 --*--
# @Time    : 2022/9/8
# @Author  : 微信公众号：K哥爬虫
# @FileName: yrx5.py
# @Software: PyCharm
# =======================

import execjs
import requests
import re


def encrypt_yrx5():
    room_heat_all = []
    for page_num in range(1, 6):
        with open('yrx5.js', 'r', encoding='utf-8') as f:
            encrypt = f.read()
            encrypt_params = execjs.compile(encrypt).call('getParamers')
            print(encrypt_params['f'])
        headers = {
            "user-agent": "yuanrenxue,project",
        }
        cookies = {
            # 填入自己的 sessionid
            "sessionid": " your sessionid ",
            "m": encrypt_params['cookie_m'],
            "RM4hZBv0dDon443M": encrypt_params['cookie_rm4']
        }
        params = {
            "m": encrypt_params['m'],
            "f": encrypt_params['f']
        }
        url = "https://match.yuanrenxue.com/api/match/5?page=%s" % page_num
        response = requests.get(url, headers=headers, cookies=cookies, params=params)
        for i in range(10):
            value = response.json()['data'][i]
            room_heat = re.findall(r"'value': (.*?)}", str(value))[0]
            room_heat_all.append(room_heat)
    room_heat_all.sort(reverse=True)
    top_five_total = 0
    for i in range(5):
        top_five_total += int(room_heat_all[i])
    print(top_five_total)


if __name__ == '__main__':
    encrypt_yrx5()
