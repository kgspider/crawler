# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-08-12
# @Author  : 微信公众号：K哥爬虫
# @FileName: baidufanyi.py
# @Software: PyCharm
# ==================================


import re
import execjs
import requests
from urllib import parse


session = requests.session()
index_url = 'https://fanyi.baidu.com/'
lang_url = 'https://fanyi.baidu.com/langdetect'
translate_api = 'https://fanyi.baidu.com/v2transapi'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
# cookies = {
#     "BAIDUID": "624363427DBD2BFCDF0C3D6E129F5C65:FG=1"
# }


def get_params(query):
    # 获取 token 和 gtk
    session.get(url=index_url, headers=headers)
    # print(session.cookies.get_dict())
    response_index = session.get(url=index_url, headers=headers)
    token = re.findall(r"token: '([0-9a-z]+)'", response_index.text)[0]
    gtk = re.findall(r'gtk = "(.*?)"', response_index.text)[0]
    # 自动检测语言
    response_lang = session.post(url=lang_url, headers=headers, data={'query': query})
    lang = response_lang.json()['lan']
    return token, gtk, lang


def get_sign_and_token(query, gtk, lang):
    with open('baidufanyi_encrypt.js', 'r', encoding='utf-8') as f:
        baidu_js = f.read()
    sign = execjs.compile(baidu_js).call('e', query, gtk)
    translate_url = 'https://fanyi.baidu.com/#%s/en/%s' % (lang, parse.quote(query))
    acs_token = execjs.compile(baidu_js).call('ascToken', translate_url)
    return sign, acs_token


def get_result(query, lang, sign, token, acs_token):
    data = {
        'from': lang,
        'to': 'en',
        'query': query,
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': sign,
        'token': token,
    }
    headers["Acs-Token"] = acs_token
    response = session.post(url=translate_api, headers=headers, data=data)
    result = response.json()['trans_result']['data'][0]['dst']
    return result


def main():
    query = input('请输入要翻译的文字：')
    token, gtk, lang = get_params(query)
    sign, acs_token = get_sign_and_token(query, gtk, lang)
    result = get_result(query, lang, sign, token, acs_token)
    print('翻译成英文的结果为：', result)


if __name__ == '__main__':
    main()
