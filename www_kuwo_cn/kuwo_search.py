# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-11-02
# @Author  : 微信公众号：K哥爬虫
# @FileName: kuwo_search.py
# @Software: PyCharm
# ==================================


import execjs
import requests


host = "www.kuwo.cn"
index_url = "http://www.kuwo.cn/search/list"
search_url = "http://www.kuwo.cn/api/www/search/searchMusicBykeyWord"
session = requests.session()
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"


def get_get_req_id():
    with open('get_reqId.js', 'r', encoding='utf-8') as f:
        req_id_js = f.read()
    req_id = execjs.compile(req_id_js).call('getReqId')
    return req_id


def get_kw_token(music_name):
    headers = {"User-Agent": UA}
    params = {"key": music_name}
    response = session.get(url=index_url, params=params, headers=headers)
    kw_token = response.cookies.get_dict()["kw_token"]
    return kw_token


def search_music(music_name, req_id, kw_token):
    headers = {
        "Referer": index_url,
        "csrf": kw_token,
        "Host": host,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    params = {
        "key": music_name,
        "httpsStatus": 1,
        "pn": 1,
        "rn": 30,
        "reqId": req_id
    }
    response = session.get(url=search_url, params=params, headers=headers)
    print(response.text)


def main():
    music_name = input("请输入音乐名称：")
    req_id = get_get_req_id()
    kw_token = get_kw_token(music_name)
    search_music(music_name, req_id, kw_token)


if __name__ == '__main__':
    main()
