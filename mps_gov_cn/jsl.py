# =======================
# --*-- coding: utf-8 --*--
# @Time    : 2022/7/27
# @Author  : 微信公众号：K哥爬虫
# @FileName: jsl.py
# @Software: PyCharm
# =======================


import json
import re
import requests
import execjs


cookies = {}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
url = "https://www.mps.gov.cn/index.html"


def get_first_cookie():
    global cookies
    resp_first = requests.get(url=url, headers=headers)
    # 获取 cookie 值 __jsluid_s
    cookies.update(resp_first.cookies)
    # 获取第一层响应内容, AAEncode 加密
    content_first = re.findall('cookie=(.*?);location', resp_first.text)[0]
    jsl_clearance_s = execjs.eval(content_first).split(';')[0]
    # 获取 cookie 值 __jsl_clearance_s
    cookies['__jsl_clearance_s'] = jsl_clearance_s.split("=")[1]


def get_second_cookie():
    global cookies
    # 通过携带 jsluid_s 和 jsl_clearance_s 值的 cookie 获取第二层响应内容
    resp_second = requests.get(url=url, headers=headers, cookies=cookies)
    # 获取 go 字典参数
    go_params = re.findall(';go\((.*?)\)</script>', resp_second.text)[0]
    params = json.loads(go_params)
    return params


def get_third_cookie():
    with open('jsl.js', 'r', encoding='utf-8') as f:
        jsl_js = f.read()
    params = get_second_cookie()
    # 传入字典
    third_cookie = execjs.compile(jsl_js).call('cookies', params)
    cookies.update(third_cookie)


def main():
    get_first_cookie()
    get_third_cookie()
    resp_third = requests.get(url=url, headers=headers, cookies=cookies)
    resp_third.encoding = 'utf-8'
    print(resp_third.text)


if __name__ == '__main__':
    main()
