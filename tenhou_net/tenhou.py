# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-08-26
# @Author  : 微信公众号：K哥爬虫
# @FileName: tenhou.py
# @Software: PyCharm
# ==================================


import execjs


url = 'https://tenhou.net/2/?q=336m237p2479s167z3s'


def main():
    q = url.split('=')[1]
    with open('tenhou_decrypt.js', 'r', encoding='utf-8') as f:
        tenhou_js = f.read()
    data = execjs.compile(tenhou_js).call('fa', q)
    print(data)


if __name__ == '__main__':
    main()
