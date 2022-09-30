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


def get_cookie_m():
    heat_total = 0
    for page_num in range(1, 6):
        with open('yrx2.js', 'r', encoding='utf-8') as f:
            encrypt = f.read()
            cookie_m = execjs.compile(encrypt).call('getCookie')
        headers = {
            "user-agent": "yuanrenxue,project",
        }
        cookies = {
            # 填入自己的 sessionid
            "sessionid": " your sessionid ",
            "m": cookie_m
        }
        url = "https://match.yuanrenxue.com/api/match/2?page=%s" % page_num
        response = requests.get(url, headers=headers, cookies=cookies)
        for i in range(10):
            value = response.json()['data'][i]
            heat = re.findall(r"'value': (.*?)}", str(value))[0]
            heat_total += int(heat)
    print(heat_total)


if __name__ == '__main__':
    get_cookie_m()
