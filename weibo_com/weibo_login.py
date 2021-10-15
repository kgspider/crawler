# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-08-31
# @Author  : 微信公众号：K哥爬虫
# @FileName: weibo_login.py
# @Software: PyCharm
# ==================================


import re
import json
import time
import base64
import binascii

import rsa
import execjs
import requests
from lxml import etree


# 判断某些请求是否成功的标志
weibo_response_success_str = 'succ'

pre_login_url = 'https://login.sina.com.cn/sso/prelogin.php'
get_token_url = 'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)'
protection_url = 'https://passport.weibo.com/protection/index'
send_code_url = 'https://passport.weibo.com/protection/mobile/sendcode'
confirm_url = 'https://passport.weibo.com/protection/mobile/confirm'

headers = {
    'Host': 'login.sina.com.cn',
    'Referer': 'https://weibo.com/',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
session = requests.session()


def get_pre_parameter(username: str) -> dict:
    su = base64.b64encode(username.encode())
    time_now = str(int(time.time() * 1000))
    params = {
        'entry': 'weibo',
        'callback': 'sinaSSOController.preloginCallBack',
        'su': su,
        'rsakt': 'mod',
        'checkpin': 1,
        'client': 'ssologin.js(v1.4.19)',
        '_': time_now,
    }
    response = session.get(url=pre_login_url, params=params, headers=headers).text
    parameter_dict = json.loads(re.findall(r'\((.*)\)', response)[0])
    # print('1.【pre parameter】: %s' % parameter_dict)
    return parameter_dict


def get_encrypted_password(pre_parameter: dict, password: str) -> str:
    # 通过 JS 获取加密后的密码
    # with open('weibo_encrypt.js', 'r', encoding='utf-8') as f:
    #     weibo_js = f.read()
    # encrypted_password = execjs.compile(weibo_js).call('getEncryptedPassword', pre_parameter, password)
    # # print('2.【encrypted password】: %s' % encrypted_password)
    # return encrypted_password

    # 通过 Python 的 rsa 模块和 binascii 模块获取加密后的密码
    public_key = rsa.PublicKey(int(pre_parameter['pubkey'], 16), int('10001', 16))
    text = '%s\t%s\n%s' % (pre_parameter['servertime'], pre_parameter['nonce'], password)
    encrypted_str = rsa.encrypt(text.encode(), public_key)
    encrypted_password = binascii.b2a_hex(encrypted_str).decode()
    # print('2.【encrypted password】: %s' % encrypted_password)
    return encrypted_password


def get_token(encrypted_password: str, pre_parameter: dict, username: str) -> str:
    su = base64.b64encode(username.encode())
    data = {
        'entry': 'weibo',
        'gateway': 1,
        'from': '',
        'savestate': 7,
        'qrcode_flag': False,
        'useticket': 1,
        'pagerefer': '',
        'vsnf': 1,
        'su': su,
        'service': 'miniblog',
        'servertime': pre_parameter['servertime'],
        'nonce': pre_parameter['nonce'],
        'pwencode': 'rsa2',
        'rsakv': pre_parameter['rsakv'],
        'sp': encrypted_password,
        'sr': '1920*1080',
        'encoding': 'UTF-8',
        'prelt': 38,
        'url': 'https://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
        'returntype': 'META'
    }
    response = session.post(url=get_token_url, headers=headers, data=data)
    # response.encoding = 'gbk'
    ajax_login_url = re.findall(r'replace\("(.*)"\)', response.text)[0]
    token = ajax_login_url.split('token%3D')[-1]
    if 'weibo' not in token:
        # print('3.【token】: %s' % token)
        return token
    else:
        raise Exception('登录失败! 用户名或者密码错误!')


def get_encrypted_mobile(token: str) -> str:
    params = {
        'token': token,
        'callback_url': 'https://weibo.com'
    }
    response = session.get(url=protection_url, params=params, headers=headers)
    tree = etree.HTML(response.text)
    encrypted_mobile = tree.xpath("//input[@name='encrypt_mobile']/@value")[0]
    # print('4.【encrypted mobile】: %s' % encrypted_mobile)
    return encrypted_mobile


def send_code(token: str, encrypt_mobile: str) -> str:
    params = {'token': token}
    data = {'encrypt_mobile': encrypt_mobile}
    response = session.post(url=send_code_url, params=params, data=data, headers=headers).json()
    if response['msg'] == weibo_response_success_str:
        code = input('请输入验证码: ')
        # print('5.【code】: %s' % code)
        return code
    else:
        # print('5.【failed to send verification code】: %s' % response)
        raise Exception('验证码发送失败: %s' % response)


def confirm_code(encrypted_mobile: str, code: str, token: str) -> str:
    params = {'token': token}
    data = {
        'encrypt_mobile': encrypted_mobile,
        'code': code
    }
    response = session.post(url=confirm_url, params=params, data=data, headers=headers).json()
    if response['msg'] == weibo_response_success_str:
        redirect_url = response['data']['redirect_url']
        # print('6.【redirect url】: %s' % redirect_url)
        return redirect_url
    else:
        # print('6.【验证码校验失败】: %s' % response)
        raise Exception('验证码校验失败: %s' % response)


def get_cross_domain2_url(redirect_url: str) -> str:
    response = session.get(url=redirect_url, headers=headers).text
    cross_domain2_url = re.findall(r'replace\("(.*)"\)', response)[0]
    # print('7.【cross domain2 url】: %s' % cross_domain2_url)
    return cross_domain2_url


def get_passport_url(cross_domain2_url: str) -> str:
    response = session.get(url=cross_domain2_url, headers=headers).text
    passport_url_str = re.findall(r'setCrossDomainUrlList\((.*)\)', response)[0]
    passport_url = json.loads(passport_url_str)['arrURL'][0]
    # print('8.【passport url】: %s' % passport_url)
    return passport_url


def login(passport_url: str) -> None:
    response = session.get(url=passport_url, headers=headers).text
    login_result = json.loads(response.replace('(', '').replace(');', ''))
    if login_result['result']:
        user_unique_id = login_result['userinfo']['uniqueid']
        user_display_name = login_result['userinfo']['displayname']
        print('登录成功！用户 ID：%s，用户名：%s' % (user_unique_id, user_display_name))
    else:
        raise Exception('登录失败：%s' % login_result)


def main():
    username = input('请输入登录账号: ')
    password = input('请输入登录密码: ')

    # 1.预登陆，获取一个字典参数，包含后面要用的 servertime、nonce、pubkey、rsakv
    pre_parameter = get_pre_parameter(username)

    # 2.通过 JS 或者 Python 获取加密后的密码
    encrypted_password = get_encrypted_password(pre_parameter, password)

    # 3.获取 token
    token = get_token(encrypted_password, pre_parameter, username)

    # 4.通过 protection url 获取加密后的手机号
    encrypted_mobile = get_encrypted_mobile(token)

    # 5.发送手机验证码
    code = send_code(token, encrypted_mobile)

    # 6.校验验证码，校验成功则返回一个重定向的 URL
    redirect_url = confirm_code(encrypted_mobile, code, token)

    # 7.访问重定向的 URL，提取 crossdomain2 URL
    cross_domain2_url = get_cross_domain2_url(redirect_url)

    # 8.访问 crossdomain2 URL，提取 passport URL
    passport_url = get_passport_url(cross_domain2_url)

    # 9.访问 passport URL 进行登录操作
    login(passport_url)


if __name__ == '__main__':
    main()
