# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-11-03
# @Author  : 微信公众号：K哥爬虫
# @FileName: nhsa.py
# @Software: PyCharm
# ==================================


import execjs
import requests


regn_code_url = "https://fuwu.nhsa.gov.cn/ebus/fuwu/api/nthl/api/dic/queryAdmdvsTree"
lv_and_type_url = "https://fuwu.nhsa.gov.cn/ebus/fuwu/api/nthl/api/fixed/queryDicByType"
result_url = "https://fuwu.nhsa.gov.cn/ebus/fuwu/api/nthl/api/fixed/queryFixedHospital"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"

with open('nhsa.js', 'r', encoding='utf-8') as f:
    nhsa_js = execjs.compile(f.read())


def get_headers():
    """获取 header 参数，每次请求改变"""
    headers = nhsa_js.call("getHeaders")
    headers["User-Agent"] = UA
    headers["Content-Type"] = "application/json"
    headers["Host"] = "fuwu.nhsa.gov.cn"
    headers["Origin"] = "https://fuwu.nhsa.gov.cn"
    headers["Referer"] = "https://fuwu.nhsa.gov.cn/nationalHallSt/"
    # print(headers)
    return headers


def get_regn_code():
    """获取城市代码，返回结果无加密"""
    payload = {"data": {"transferFlag": ""}}
    response = requests.post(url=regn_code_url, json=payload, headers=get_headers())
    print(response.text)


def get_medins_lv_or_type_code(key):
    """获取医疗机构等级 (LV) or 类型 (TYPE) 代码"""
    if key == "LV":
        payload = {"type": "MEDINSLV"}
    elif key == "TYPE":
        payload = {"type": "MEDINS_TYPE"}
    else:
        print("输入有误!")
        return
    encrypted_payload = nhsa_js.call("getEncryptedData", payload)
    encrypted_data = requests.post(url=lv_and_type_url, json=encrypted_payload, headers=get_headers()).json()
    decrypted_data = nhsa_js.call("getDecryptedData", encrypted_data)
    print(decrypted_data)


def get_result():
    addr = input("请输入医疗机构详细地址(默认无): ") or ""
    medins_lv_code = input("请输入医疗机构等级代码(默认无): ") or ""
    medins_name = input("请输入医疗机构名称(默认无): ") or ""
    medins_type_code = input("请输入医疗机构类型代码(默认无): ") or ""
    regn_code = input("请输入医疗机构所在地代码(默认北京市): ") or "110000"
    page_num = input("请输入要爬取的页数(默认1): ") or 1

    for page in range(1, int(page_num)+1):
        payload = {
            "addr": addr,
            "medinsLvCode": medins_lv_code,
            "medinsName": medins_name,
            "medinsTypeCode": medins_type_code,
            "pageNum": page,
            "pageSize": 10,
            "regnCode": regn_code,
            "sprtEcFlag": ""
        }
        page += 1
        encrypted_payload = nhsa_js.call("getEncryptedData", payload)
        encrypted_data = requests.post(url=result_url, json=encrypted_payload, headers=get_headers()).json()
        decrypted_data = nhsa_js.call("getDecryptedData", encrypted_data)
        print(decrypted_data)


def main():
    # 获取城市代码
    # get_regn_code()
    # 获取医疗机构等级代码
    # get_medins_lv_or_type_code("LV")
    # 获取医疗机构类型代码
    # get_medins_lv_or_type_code("TYPE")
    # 获取搜索结果
    get_result()


if __name__ == "__main__":
    main()
