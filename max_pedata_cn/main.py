# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-12-31
# @Author  : 微信公众号：K哥爬虫
# @FileName: main.py
# @Software: PyCharm
# ==================================


import execjs
import requests

news_est_url = "https://max.pedata.cn/api/q4x/newsflash/list"
login_token = "1796a48fa1968edd5xxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # token 换成你自己的
headers = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "Host": "max.pedata.cn",
    "HTTP-X-TOKEN": login_token,
    "Origin": "https://max.pedata.cn",
    "Referer": "https://max.pedata.cn/client/news/newsflash",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}


def get_decrypted_data(encrypted_data, exor):
    with open('pedata_decrypt.js', 'r', encoding='utf-8') as f:
        pedata_js = f.read()
    decrypted_data = execjs.compile(pedata_js).call('getDecryptedData', encrypted_data, exor, login_token)
    return decrypted_data


def get_encrypted_data():
    data = {
        "type": "",
        "module": "LP",
        "page":
            {
                "currentPage": 1,
                "pageSize": 10
            }
    }
    response = requests.post(url=news_est_url, headers=headers, json=data).json()
    encrypted_data, exor = response["data"], response["exor"]
    return encrypted_data, exor


def main():
    encrypted_data, exor = get_encrypted_data()
    decrypted_data = get_decrypted_data(encrypted_data, exor)
    print(decrypted_data)


if __name__ == '__main__':
    main()
