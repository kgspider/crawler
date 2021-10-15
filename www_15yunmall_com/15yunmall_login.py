# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-08-19
# @Author  : 微信公众号：K哥爬虫
# @FileName: 15yunmall_login.py
# @Software: PyCharm
# ==================================


import execjs
import requests

from lxml import etree
from PIL import Image


index_url = 'http://www.15yunmall.com/pc/login/index'
login_url = 'http://www.15yunmall.com/pc/login/check'
code_url = 'http://www.15yunmall.com/very/code.html'

headers = {
    'Host': 'www.15yunmall.com',
    'Referer': 'http://www.15yunmall.com/',
    'Origin': 'http://www.15yunmall.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}
session = requests.session()


def get_encrypted_password(password):
    with open('15yunmall_encrypt.js', 'r', encoding='utf-8') as f:
        yunmall_js = f.read()
    encrypted_password = execjs.compile(yunmall_js).call('getEncryptedPassword', password)
    return encrypted_password


def get_csrf_token_cookie():
    response = session.get(url=index_url, headers=headers)
    tree = etree.HTML(response.text)
    csrf_token = tree.xpath("//input[@name='_csrfToken']/@value")[0]
    cookies = response.cookies.get_dict()
    # print(csrf_token, cookies)
    return csrf_token, cookies


def get_very_code(cookies):
    response = session.get(url=code_url, cookies=cookies, headers=headers)
    with open('code.png', 'wb') as f:
        f.write(response.content)
    image = Image.open('code.png')
    image.show()
    very_code = input('请输入验证码: ')
    return very_code


def login(csrf_token, very_code, cookies, username, encrypted_password):
    data = {
        'u[loginType]': 'name',
        'u[phone]': username,
        'u[password]': encrypted_password,
        'u[veryCode]': very_code,
        'u[token]': '',
        '_csrfToken': csrf_token
    }
    header_info = {
        'X-Requested-With': 'XMLHttpRequest',
    }
    headers.update(header_info)
    response = session.post(url=login_url, data=data, cookies=cookies, headers=headers)
    response.encoding = 'utf-8-sig'
    response_code = response.text
    # print(response_code)
    status_code = {
        '31': '恭喜，登陆成功。',
        '32': '登陆失败。',
        '33': '用户名或密码错误。',
        '35': '该用户已被管理员锁定。',
        '311': '该账号已绑定设备，请在绑定的设备登陆。',
        '20001': '验证码填写错误!'
    }
    try:
        print(status_code[response_code])
    except KeyError:
        print('请求超时！')


def main():
    username = input('请输入登录账号: ')
    password = input('请输入登录密码: ')
    if len(password) > 32:
        raise Exception('请输入正确的密码！')
    encrypted_password = get_encrypted_password(password)
    csrf_token, cookies = get_csrf_token_cookie()
    very_code = get_very_code(cookies)
    login(csrf_token, very_code, cookies, username, encrypted_password)


if __name__ == '__main__':
    main()
