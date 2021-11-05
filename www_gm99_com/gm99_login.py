# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-10-28
# @Author  : 微信公众号：K哥爬虫
# @FileName: gm99_login.py
# @Software: PyCharm
# ==================================


import re
import json
import time
import random
import base64
from urllib import parse

import execjs
import requests
from PIL import Image
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5

login_url = 'https://passport.gm99.com/login/login3'
verify_image_url = 'https://passport.gm99.com/verify_image'
check_code_url = 'https://passport.gm99.com/ajax/check_code'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
session = requests.session()


def get_jquery():
    jsonp = ''
    for _ in range(21):
        jsonp += str(random.randint(0, 9))
    jquery = 'jQuery' + jsonp + '_'
    return jquery


def get_dict_from_jquery(text):
    result = re.findall(r'\((.*?)\)', text)[0]
    return json.loads(result)


def get_encrypted_password_by_javascript(password):
    # 两个 JavaScript 脚本，两种方法均可
    with open('gm99_encrypt.js', 'r', encoding='utf-8') as f:
    # with open('gm99_encrypt_2.js', 'r', encoding='utf-8') as f:
        exec_js = f.read()
    encrypted_password = execjs.compile(exec_js).call('getEncryptedPassword', password)
    return encrypted_password


def get_encrypted_password_by_python(password):
    timestamp = str(int(time.time() * 1000))
    encrypted_object = timestamp + "|" + password
    public_key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDq04c6My441Gj0UFKgrqUhAUg+kQZeUeWSPlAU9fr4HBPDldAeqzx1UR92KJHuQh/zs1HOamE2dgX9z/2oXcJaqoRIA/FXysx+z2YlJkSk8XQLcQ8EBOkp//MZrixam7lCYpNOjadQBb2Ot0U/Ky+jF2p+Ie8gSZ7/u+Wnr5grywIDAQAB"
    rsa_key = RSA.import_key(base64.b64decode(public_key))  # 导入读取到的公钥
    cipher = PKCS1_v1_5.new(rsa_key)                        # 生成对象
    encrypted_password = base64.b64encode(cipher.encrypt(encrypted_object.encode(encoding="utf-8")))
    encrypted_password = parse.quote(encrypted_password)
    return encrypted_password


def get_verify_code():
    response = session.get(url=verify_image_url, headers=headers)
    with open('code.png', 'wb') as f:
        f.write(response.content)
    image = Image.open('code.png')
    image.show()
    code = input('请输入图片验证码: ')
    return code


def check_code(code):
    timestamp = str(int(time.time() * 1000))
    params = {
        'callback': get_jquery() + timestamp,
        'ckcode': code,
        '_': timestamp,
    }
    response = session.get(url=check_code_url, params=params, headers=headers)
    result = get_dict_from_jquery(response.text)
    if result['result'] == 1:
        pass
    else:
        raise Exception('验证码输入错误！')


def login(username, encrypted_password, code):
    timestamp = str(int(time.time() * 1000))
    params = {
        'callback': get_jquery() + timestamp,
        'encrypt': 1,
        'uname': username,
        'password': encrypted_password,
        'remember': 'checked',
        'ckcode': code,
        '_': timestamp
    }
    response = session.get(url=login_url, params=params, headers=headers)
    result = get_dict_from_jquery(response.text)
    print(result)


def main():
    # 测试账号：15434947408，密码：iXqC@aJt8fi@VwV
    username = input('请输入登录账号: ')
    password = input('请输入登录密码: ')

    # 获取加密后的密码，使用 Python 或者 JavaScript 实现均可
    encrypted_password = get_encrypted_password_by_javascript(password)
    # encrypted_password = get_encrypted_password_by_python(password)

    # 获取验证码
    code = get_verify_code()

    # 校验验证码
    check_code(code)

    # 登录
    login(username, encrypted_password, code)


if __name__ == '__main__':
    main()
