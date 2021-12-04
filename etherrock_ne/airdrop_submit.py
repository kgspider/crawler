# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-11-24
# @Author  : 微信公众号：K哥爬虫
# @FileName: airdrop_submit.py
# @Software: PyCharm
# ==================================


import execjs
import requests


def get_content_and_key(address):
    with open("get_content_and_key.js", encoding="utf-8") as f:
        ether_rock_js = f.read()
    content_and_key_dict = execjs.compile(ether_rock_js).call('getContentAndKey', address)
    return content_and_key_dict


def airdrop_submit(content_and_key_dict):
    submit_url = "https://etherrock.net/airdrop-submit"
    headers = {
        "Accept": "text/html, */*; q=0.01",
        "Accept-Language": "zh,zh-CN;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Host": "etherrock.net",
        "Origin": "https://etherrock.net",
    }
    data = {
        "content": content_and_key_dict["content"],
        "key": content_and_key_dict["key"]
    }
    response = requests.post(url=submit_url, data=data, headers=headers)
    print(response.text)


def main():
    address = input("请输入ETH钱包地址领取空投: ")
    content_and_key_dict = get_content_and_key(address)
    airdrop_submit(content_and_key_dict)


if __name__ == '__main__':
    main()
