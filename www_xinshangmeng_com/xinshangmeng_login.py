# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-09-07
# @Author  : 微信公众号：K哥爬虫
# @FileName: xinshangmeng_login.py
# @Software: PyCharm
# ==================================


import time
import random

import execjs
import requests
from PIL import Image


index_url = 'http://www.xinshangmeng.com/xsm2/?Version=2021061900'
login_url = 'http://login.xinshangmeng.com/login/users/dologin/dfaup'
ver_code_url = 'https://login.xinshangmeng.com/login/users/forlogin/img'
headers = {
    'Referer': 'http://www.xinshangmeng.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}
session = requests.session()


def get_verification_code():
    response = session.get(url=ver_code_url, headers=headers)
    with open('code.png', 'wb') as f:
        f.write(response.content)
    image = Image.open('code.png')
    image.show()
    code = input('请输入验证码: ')
    return code


def get_encrypted_password(username, password, code):
    with open('xinshangmeng_encrypt.js', 'r', encoding='utf-8') as f:
        xinshangmeng_js = f.read()
    encrypted_password = execjs.compile(xinshangmeng_js).call('getEncryptedPassword', username, password, code)
    return encrypted_password


def login(username, encrypted_password, code):
    timestamp = str(round(time.time() * 1000))
    jsonp = ''
    for _ in range(20):
        jsonp += str(random.randint(0, 9))
    jsonp = 'jQuery' + jsonp + '_' + timestamp
    params = {
        'jsonp': jsonp,
        'protocol': ' http:',
        'loginIndex': index_url,
        'j_mmrm': username,
        'j_mcmm': encrypted_password,
        'j_valcode': code,
        '_': timestamp
    }
    response = session.get(url=login_url, params=params, headers=headers)
    response.encoding = 'utf-8'
    print(response.text)


def main():
    username = input('请输入登录账号: ')
    password = input('请输入登录密码: ')
    code = get_verification_code()
    encrypted_pwd = get_encrypted_password(username, password, code)
    login(username, encrypted_pwd, code)


if __name__ == '__main__':
    main()
