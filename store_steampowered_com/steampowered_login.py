# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-09-09
# @Author  : 微信公众号：K哥爬虫
# @FileName: steampowered_login.py
# @Software: PyCharm
# ==================================


import time

import execjs
import requests
from PIL import Image


index_url = 'https://store.steampowered.com/login'
login_url = 'https://store.steampowered.com/login/dologin/'
get_rsa_key_url = 'https://store.steampowered.com/login/getrsakey/'
render_captcha_url = 'https://store.steampowered.com/login/rendercaptcha/'
refresh_captcha_url = 'https://store.steampowered.com/login/refreshcaptcha/'

headers = {
    'Host': 'store.steampowered.com',
    'Origin': 'https://store.steampowered.com',
    'Referer': 'https://store.steampowered.com/login',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
session = requests.session()


def get_cookies():
    response = session.get(url=index_url, headers=headers)
    cookies = response.cookies.get_dict()
    print(cookies)
    return cookies


def get_captcha(cookies):
    # 首先获取 gid
    data = {'donotcache': str(int(time.time() * 1000))}
    refresh_captcha_response = session.post(url=refresh_captcha_url, data=data, cookies=cookies, headers=headers)
    gid = refresh_captcha_response.json()['gid']

    # 携带 gid 获取验证码
    params = {'gid': gid}
    render_captcha_response = session.get(url=render_captcha_url, params=params, cookies=cookies, headers=headers)

    with open('code.png', 'wb') as f:
        f.write(render_captcha_response.content)
    image = Image.open('code.png')
    image.show()
    captcha = input('请输入验证码: ')
    return captcha, gid


def get_rsa_key(username, cookies):
    data = {
        'donotcache': str(int(time.time() * 1000)),
        'username': username
    }
    response = session.post(url=get_rsa_key_url, data=data, cookies=cookies, headers=headers).json()
    print(response)
    return response


def get_encrypted_password(password, rsa_key_dict):
    with open('steampowered_encrypt.js', 'r', encoding='utf-8') as f:
        steampowered_js = f.read()
    encrypted_password = execjs.compile(steampowered_js).call('getEncryptedPassword', password, rsa_key_dict)
    print(encrypted_password)
    return encrypted_password


def login(username, encrypted_password, cookies, rsa_key_dict, captcha, gid):
    data = {
        'donotcache': str(int(time.time() * 1000)),
        'password': encrypted_password,
        'username': username,
        'twofactorcode': '',
        'emailauth': '',
        'loginfriendlyname': '',
        'captchagid': gid,
        'captcha_text': captcha,
        'emailsteamid': '',
        'rsatimestamp': rsa_key_dict['timestamp'],
        'remember_login': False,
        # 'tokentype': '-1'
    }
    print(data)
    response = session.post(url=login_url, data=data, cookies=cookies, headers=headers)
    print(response.text)


def main():
    username = input('请输入登录账号: ')
    password = input('请输入登录密码: ')

    # 获取 cookies
    cookies = get_cookies()

    # 获取验证码和 gid
    captcha, gid = get_captcha(cookies)

    # 获取 RSA 加密所需 key 等信息
    rsa_key_dict = get_rsa_key(username, cookies)

    # 获取加密后的密码
    encrypted_password = get_encrypted_password(password, rsa_key_dict)

    # 携带 用户名、加密后的密码、cookies、验证码等登录
    login(username, encrypted_password, cookies, rsa_key_dict, captcha, gid)


if __name__ == '__main__':
    main()
