# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-11-05
# @Author  : 微信公众号：K哥爬虫
# @FileName: cnki.py
# @Software: PyCharm
# ==================================


import execjs
import requests


token_url = "https://dict.cnki.net/fyzs-front-api/getToken"
translation_api = "https://dict.cnki.net/fyzs-front-api/translate/literaltranslation"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"

session = requests.session()


def get_token():
    headers = {"User-Agent": UA}
    response = session.get(url=token_url, headers=headers).json()
    token = response["data"]
    return token


def get_encrypted_word(word):
    with open('cnki_encrypt.js', 'r', encoding='utf-8') as f:
        cnki_js = f.read()
    encrypted_word = execjs.compile(cnki_js).call('s', word)
    return encrypted_word


def get_translation_result(encrypted_word, token):
    payload = {
        "translateType": None,
        "words": encrypted_word
    }
    headers = {
        "Token": token,
        "User-Agent": UA
    }
    response = session.post(url=translation_api, headers=headers, json=payload).json()
    result = response["data"]["mResult"]
    return result


def main():
    word = input("请输入待翻译字符串: ")
    token = get_token()
    encrypted_word = get_encrypted_word(word)
    result = get_translation_result(encrypted_word, token)
    print("翻译结果为: ", result)


if __name__ == "__main__":
    main()
