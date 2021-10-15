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


index_url = 'https://fanyi.baidu.com/'
lang_url = 'https://fanyi.baidu.com/langdetect'
translate_api = 'https://fanyi.baidu.com/v2transapi'
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh,zh-CN;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=3BE16D933E9C0182F2A6E93D7A9D1424; PSTM=1623723330; BAIDUID=8496908995397662040287D2CE1C4224:FG=1; __yjs_duid=1_779078c2c847bb3217554b8549ad49bd1623728424311; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDSFRCVID_BFESS=BkFOJeCT5G3_WP5eFqJ2T4D2p2KKN9OTTPjcTR5qJ04BtyCVNKsaEG0PtOgMNBDbJ2MRogKKLgOTHULF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJ4toCPMJI_3fP36q45HMt00qxby26PDajn9aJ5nQI5nhU7505oqDJ0Z0ROOWhRute3i2DTvQUbmjRO206oay6O3LlO83h5wW57KKl0MLPbcep68LxODy6DI0xnMBMnr52OnaU513fAKftnOM46JehL3346-35543bRTLnLy5KJYMDF4D5_ae5O3DGRf-b-XKD600PK8Kb7VbUF6qfnkbft7jtteyhbTJCID-UQKQPnc_pC4yURFef473b3B5h3NJ66ZoIbPbPTTSlroKPQpQT8r5-nMWx6G3IrZoq64ab3vOpRTXpO13fAzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksD-FtqjDjJRCOoI--f-3bfTrP-trf5DCShUFs3tnlB2Q-5M-a3KOrSUtGbfjay6D7j-8HbTjiW2_82MbmLncjSM_GKfC2jMD32tbpWfneKmTxoUJ2Bb3Y8loe-xCKXqDebPRiWPb9QgbP2pQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHjKbDTvL3f; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1624438637,1624603638,1624928461,1624953786; H_PS_PSSID=34131_34099_31253_34004_33607_34107_34135; delPer=0; PSINO=6; BAIDUID_BFESS=8496908995397662040287D2CE1C4224:FG=1; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1624962661; __yjs_st=2_MzJhZTMxZGU5MjZjNGJiZTJiZjQwYjVkMWM5ZjYyMGFjZDlkMDJmNTU3OGU5ZTM4N2JjNjNkODAwYWJiY2M3NDA1NWEyODNkMzNkMDEzNThiZTU4NzNhMTQxYzIxOTQyMzg3MjhiMzA5ZjY2MDczZTBhZDdmZDg4YTFhNjVmZTMwZTYyZTRjNmRhMWNmYzg3NDFjODYzYTRlZTE2NzBmODAyMWI4MTI3NTZmNjg1MDk4OWIxZTYzNTc4NzhjY2E3NzU3ZGYyZmI1ODdjZTM5ZDNlOGU0ZGQ2NzE5OGU2NzUzM2ZhZTcxZmVjNjI4MDIyN2Y1N2NlMzZmMmRlY2U4Yl83XzQ5NzQ4ZWE4; ab_sr=1.0.1_MmUwODU0NGE4NjIwZmY4NjgxZmM1NGYxOTI5ZWQwOGU2NjU3ZjgwNzhkMTNjNDI5NWE0ODQwYzlkZDVjY2Q1YWEyZDQyZWI0ZjNkMWQ0NTEyMGFjYzdiNDdmNzYxYjNiMjkxZTI1M2I3Y2VhZGE3NDEzOTgyMjY1MjBlZGM4OGJiZGVjMzFkYTM3ODgyMTRkZjJhMGYzNGM0MGJmMGY1Yg==',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


def get_token():
    response = requests.get(url=index_url, headers=headers).text
    token = re.findall(r"token: '([0-9a-z]+)", response)[0]
    return token


def get_sign(query):
    with open('baidu_encrypt.js', 'r', encoding='utf-8') as f:
        baidu_js = f.read()
    sign = execjs.compile(baidu_js).call('e', query)
    return sign


def get_result(lang, query, sign, token):
    data = {
        'from': lang,
        'to': 'en',
        'query': query,
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': sign,
        'token': token,
    }
    response = requests.post(url=translate_api, headers=headers, data=data)
    result = response.json()['trans_result']['data'][0]['dst']
    return result


def main():
    query = input('请输入要翻译的文字：')
    response = requests.post(url=lang_url, headers=headers, data={'query': query})
    lang = response.json()['lan']
    token = get_token()
    sign = get_sign(query)
    result = get_result(lang, query, sign, token)
    print('翻译成英文的结果为：', result)


if __name__ == '__main__':
    main()
