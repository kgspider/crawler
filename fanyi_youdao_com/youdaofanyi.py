# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-08-13
# @Author  : 微信公众号：K哥爬虫
# @FileName: youdaofanyi.py
# @Software: PyCharm
# ==================================


import time
import random
import hashlib

import execjs
import requests


translate_url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'


def get_translation_result(parameters):
    headers = {
        'User-Agent': user_agent,
        'Host': 'fanyi.youdao.com',
        'Origin': 'https://fanyi.youdao.com',
        'Referer': 'https://fanyi.youdao.com/',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'Cookie': 'OUTFOX_SEARCH_USER_ID="-1848382357@10.169.0.84"; ___rl__test__cookies=1625907853887; OUTFOX_SEARCH_USER_ID_NCOO=132978720.55854891'
    }
    response = requests.post(url=translate_url, headers=headers, data=parameters)
    result = response.json()['translateResult'][0][0]['tgt']
    return result


def get_parameters_by_python(query, translate_from, translate_to):
    lts = str(int(time.time() * 1000))                                # 以毫秒为单位的 13 位时间戳
    salt = lts + str(random.randint(0, 9))                            # 13 位时间戳+随机数字，生成 salt 值
    sign = "fanyideskweb" + query + salt + "Y2FYu%TNSbMCxc3t2u^XT"    # 拼接字符串组成 sign
    sign = hashlib.md5(sign.encode()).hexdigest()                     # 将 sign 进行 MD5 加密，生成最终 sign 值
    bv = hashlib.md5(user_agent.encode()).hexdigest()                 # 对 UA 进行 MD5 加密，生成 bv 值
    parameters = {
        'i': query,
        'from': translate_from,
        'to': translate_to,
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'lts': lts,
        'bv': bv,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    return parameters


def get_parameters_by_javascript(query, translate_from, translate_to):
    with open('youdao_encrypt.js', 'r', encoding='utf-8') as f:
        youdao_js = f.read()
    params = execjs.compile(youdao_js).call('get_params', query, user_agent)    # 通过 JavaScript 代码获取各个参数
    bv = hashlib.md5(user_agent.encode()).hexdigest()                           # 对 UA 进行 MD5 加密，生成 bv 值
    parameters = {
        'i': query,
        'from': translate_from,
        'to': translate_to,
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': params['salt'],
        'sign': params['sign'],
        'lts': params['lts'],
        'bv': bv,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    return parameters


def main():
    query = input('请输入要翻译的文字：')
    # 原始语言，目标语言，默认自动处理
    translate_from = translate_to = 'AUTO'
    # 通过 Python 获取加密参数或者通过 JavaScript 获取参数，二选一
    param = get_parameters_by_python(query, translate_from, translate_to)
    # param = get_parameters_by_javascript(query, translate_from, translate_to)
    result = get_translation_result(param)
    print('翻译的结果为：', result)


if __name__ == '__main__':
    main()
