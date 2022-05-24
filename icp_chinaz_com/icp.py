# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2022-05-18
# @Author  : 微信公众号：K哥爬虫
# @FileName: icp.py
# @Software: PyCharm
# ==================================


import execjs
import requests


headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "icp.chinaz.com",
    "Origin": "http://icp.chinaz.com",
    "Referer": "http://icp.chinaz.com/itbob.cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

kw = "baidu.com"
url = "http://icp.chinaz.com/home/GetPerimitByHost"

with open('generatetokenNew.js', 'r', encoding='utf-8') as f:
    icp_js = f.read()
hostToken = execjs.compile(icp_js).call('generateHostKey', kw)
permitToken = execjs.compile(icp_js).call('generateWordKey', kw)

data = {
    "kw": kw,
    "hostToken": hostToken,
    "permitToken": permitToken
}

print("data: ", data)
response = requests.post(url=url, headers=headers, data=data)
print("response: ", response.json())
