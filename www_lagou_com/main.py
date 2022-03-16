# =============================================
# --*-- coding: utf-8 --*--
# @Time    : 2022-03-03
# @Author  : 微信公众号：K哥爬虫
# @FileName: main.py
# @Software: PyCharm
# @notice  : 有些参数并不是必须的，写死或者不要都行，
#            文章中有说明，可根据你实际情况自行修改
# =============================================


import time
import json
import execjs
import requests
from lxml import etree
from urllib import parse


aes_key = ""
secret_key_value = ""

with open('lagou.js', 'r', encoding='utf-8') as f:
    lagou_js = execjs.compile(f.read())

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"

x_anit = {
    "x-anit-forge-code": "0",
    "x-anit-forge-token": None
}

global_cookies = {
    # - 如果 IP 被拉黑，访问需要登录，或者提示太频繁，那么就需要那么就需要补全登录后的 cookie！
    # - 以下所有值都必须在登录后再复制过来，特别是 JSESSIONID，没登录得到的 JSESSIONID 是无效的！
    # - 经过测试主要是以下三个 cookie 起作用，能保持登录：login、gate_login_token、_putrc
    # - 还有一个 JSESSIONID 值，主要是用来获取请求头 x-anit-forge-code 和 x-anit-forge-token

    # "login": "true",
    # "gate_login_token": "",
    # "_putrc": "",
    # "JSESSIONID": ""
}


def get_user_trace_token() -> str:
    # 获取 cookie 中的 user_trace_token
    json_url = "https://a.lagou.com/json"
    headers = {
        "Host": "a.lagou.com",
        "Referer": "https://www.lagou.com/",
        "User-Agent": UA
    }
    params = {
        "lt": "trackshow",
        "t": "ad",
        "v": 0,
        "dl": "https://www.lagou.com/",
        "dr": "https://www.lagou.com",
        "time": str(int(time.time() * 1000))
    }
    response = requests.get(url=json_url, headers=headers, params=params)
    user_trace_token = response.cookies.get_dict()["user_trace_token"]
    return user_trace_token


def get_lg_stoken(original_data: dict) -> str:
    # 获取 cookie 中的 __lg_stoken__
    token_url = "https://www.lagou.com/wn/jobs"
    token_headers = {
        "Host": "www.lagou.com",
        "Referer": "https://www.lagou.com/",
        "User-Agent": UA
    }
    params = {
        "kd": original_data["kd"],
        "city": original_data["city"]
    }
    token_response = requests.get(url=token_url, params=params, headers=token_headers, cookies=global_cookies, allow_redirects=False)
    if token_response.status_code != 302:
        raise Exception("获取跳转链接异常！检查 global_cookies 是否已包含 __lg_stoken__！")
    # 获取 302 跳转的地址
    security_check_url = token_response.headers["Location"]
    if "login" in security_check_url:
        raise Exception("IP 被关进小黑屋啦！需要登录！请补全登录后的 Cookie，或者自行添加代理！")
    parse_result = parse.urlparse(security_check_url)
    # url 的参数为待加密对象
    security_check_params = parse_result.query
    # 取 name 参数，为混淆 js 的文件名
    security_check_js_name = parse.parse_qs(security_check_params)["name"][0]

    # 发送请求，获取混淆的 js
    js_url = "https://www.lagou.com/common-sec/dist/" + security_check_js_name + ".js"
    js_headers = {
        "Host": "www.lagou.com",
        "Referer": security_check_url,
        "User-Agent": UA
    }
    js_response = requests.get(url=js_url, headers=js_headers, cookies=global_cookies).text
    # 补全 js，添加 window 参数和一个方法，用于获取 __lg_stoken__ 的值
    lg_js = """
    window = {
        "location": {
            "hostname": "www.lagou.com",
            "search": '?%s'
        }
    }
    function getLgStoken(){
        return window.gt.prototype.a()
    }
    """ % security_check_params + js_response

    lg_stoken = execjs.compile(lg_js).call("getLgStoken")
    return lg_stoken


def update_cookies(original_data: dict) -> None:
    global global_cookies
    # 获取 user_trace_token
    user_trace_token = get_user_trace_token()
    # 获取 X_HTTP_TOKEN
    x_http_token = lagou_js.call("getXHttpToken", "user_trace_token=" + user_trace_token)
    # 第一次更新全局 cookies，后续获取 __lg_stoken__ 会用到
    global_cookies.update({
        "user_trace_token": user_trace_token,
        "X_HTTP_TOKEN": x_http_token
    })

    # 获取 __lg_stoken__
    lg_stoken = get_lg_stoken(original_data)
    # 第二次更新全局 cookies
    global_cookies.update({
        "__lg_stoken__": lg_stoken,
    })


def update_aes_key() -> None:
    # 通过JS获取 AES Key，并通过接口激活，接口激活后会返回一个 secretKeyValue，后续请求头会用到
    global aes_key, secret_key_value
    url = "https://gate.lagou.com/system/agreement"
    headers = {
        "Content-Type": "application/json",
        "Host": "gate.lagou.com",
        "Origin": "https://www.lagou.com",
        "Referer": "https://www.lagou.com/",
        "User-Agent": UA
    }
    encrypt_data = lagou_js.call("getAesKeyAndRsaEncryptData")
    aes_key = encrypt_data["aesKey"]
    rsa_encrypt_data = encrypt_data["rsaEncryptData"]
    data = {"secretKeyDecode": rsa_encrypt_data}
    response = requests.post(url=url, headers=headers, json=data).json()
    secret_key_value = response["content"]["secretKeyValue"]


def update_x_anit(original_data: dict) -> None:
    # 更新 x-anit-forge-code 和 x-anit-forge-token
    url = "https://www.lagou.com/wn/jobs"
    headers = {
        "Host": "www.lagou.com",
        "Referer": "https://www.lagou.com/",
        "User-Agent": UA
    }
    params = {
        "kd": original_data["kd"],
        "city": original_data["city"]
    }
    response = requests.get(url=url, params=params, headers=headers, cookies=global_cookies)
    tree = etree.HTML(response.text)
    next_data_json = json.loads(tree.xpath("//script[@id='__NEXT_DATA__']/text()")[0])
    submit_code = next_data_json["props"]["tokenData"]["submitCode"]
    submit_token = next_data_json["props"]["tokenData"]["submitToken"]
    # 注意 JSESSIONID 必须是登录验证后的！
    if not submit_code or not submit_token:
        raise Exception("submitCode & submitToken 为空，请检查 JSESSIONID 是否正确！")
    global x_anit
    x_anit["x-anit-forge-code"] = submit_code
    x_anit["x-anit-forge-token"] = submit_token


def get_header_params(original_data: dict) -> dict:
    # 后续请求数据所需的请求头参数
    # 职位搜索 URL，如果是搜索公司，那就是 https://www.lagou.com/jobs/companyAjax.json，根据实际情况更改
    u = "https://www.lagou.com/jobs/v2/positionAjax.json"
    return {
        "traceparent": lagou_js.call("getTraceparent"),
        "X-K-HEADER": secret_key_value,
        "X-S-HEADER": lagou_js.call("getXSHeader", aes_key, original_data, u),
        "X-SS-REQ-HEADER": json.dumps({"secret": secret_key_value})
    }


def get_encrypted_data(original_data: dict) -> str:
    # AES 加密原始数据
    encrypted_data = lagou_js.call("getRequestData", aes_key, original_data)
    return encrypted_data


def get_data(original_data: dict, encrypted_data: str, header_params: dict) -> dict:
    # 携带加密后的请求数据和完整请求头，拿到密文，AES 解密得到明文职位信息
    url = "https://www.lagou.com/jobs/v2/positionAjax.json"
    referer = parse.urljoin("https://www.lagou.com/wn/jobs?", parse.urlencode(original_data))
    headers = {
        # "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "www.lagou.com",
        "Origin": "https://www.lagou.com",
        "Referer": referer,
        "traceparent": header_params["traceparent"],
        "User-Agent": UA,
        "X-K-HEADER": header_params["X-K-HEADER"],
        "X-S-HEADER": header_params["X-S-HEADER"],
        "X-SS-REQ-HEADER": header_params["X-SS-REQ-HEADER"],
    }
    # 添加 x-anit-forge-code 和 x-anit-forge-token
    headers.update(x_anit)

    data = {"data": encrypted_data}
    response = requests.post(url=url, headers=headers, cookies=global_cookies, data=data).json()
    if "status" in response:
        if not response["status"] and "操作太频繁" in response["msg"]:
            raise Exception("获取数据失败！msg：%s！可以尝试补全登录后的 Cookies，或者添加代理！" % response["msg"])
        else:
            raise Exception("获取数据异常！请检查数据是否完整！")
    else:
        response_data = response["data"]
        decrypted_data = lagou_js.call("getResponseData", response_data, aes_key)
        return decrypted_data


def main():
    # 初始化设置标识
    need_init = True

    # 要搜索的原始数据，例如爬取最新的10页全国Java岗位
    for pn in range(1, 10):
        original_data = {
            "city": "全国",   # 城市范围
            "pn": pn,        # 页码
            "kd": "Java",    # 关键词
            "px": "new"      # 排序方式，new：最新，default：默认
        }

        while need_init:
            # 初始化设置各项参数，这些参数只需要设置一次就行了，后续请求可以复用
            # 获取必要的 cookies，主要是 user_trace_token、X_HTTP_TOKEN、__lg_stoken__
            update_cookies(original_data)
            # 获取并激活 AES Key，不激活无法使用
            update_aes_key()
            # 如果登录了账号，则获取职位的请求 header 多了两个参数，x-anit-forge-code 和 x-anit-forge-token
            # 在实际测试中，不加这两个值，或者随机值都行，严谨起见还是正常获取一下
            if "login" in global_cookies:
                update_x_anit(original_data)
            need_init = False

        # 获取请求头各参数：X-K-HEADER、X-S-HEADER、X-SS-REQ-HEADER、traceparent
        header_params = get_header_params(original_data)
        # 将要搜索的原始数据进行 AES 加密
        encrypted_data = get_encrypted_data(original_data)
        # 发起请求，获取加密数据并解密成明文
        data = get_data(original_data, encrypted_data, header_params)
        print(data)


if __name__ == '__main__':
    main()
