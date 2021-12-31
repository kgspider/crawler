# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-12-29
# @Author  : 微信公众号：K哥爬虫
# @FileName: main.py
# @Software: PyCharm
# ==================================


import re
import execjs
import requests


index_url = "https://xueqiu.com/today"
news_test_url = "https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=294528&size=15"
headers = {
    "Host": "xueqiu.com",
    "Referer": "https://xueqiu.com/today",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
}


def get_complete_cookie():
    complete_cookie = {}
    # 第一次不带参数访问首页，获取 acw_tc 和 acw_sc__v2
    response = requests.get(url=index_url, headers=headers)
    complete_cookie.update(response.cookies.get_dict())
    arg1 = re.findall("arg1='(.*?)'", response.text)[0]
    with open('get_acw_sc_v2.js', 'r', encoding='utf-8') as f:
        acw_sc_v2_js = f.read()
    acw_sc__v2 = execjs.compile(acw_sc_v2_js).call('getAcwScV2', arg1)
    complete_cookie.update({"acw_sc__v2": acw_sc__v2})
    # 第二次访问首页，获取其他 cookies
    response2 = requests.get(url=index_url, headers=headers, cookies=complete_cookie)
    complete_cookie.update(response2.cookies.get_dict())
    return complete_cookie


def news_test(cookies):
    response = requests.get(url=news_test_url, headers=headers, cookies=cookies)
    print(response.json())


if __name__ == '__main__':
    complete_cookie = get_complete_cookie()
    news_test(complete_cookie)
