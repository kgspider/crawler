# =======================
# --*-- coding: utf-8 --*--
# @Time    : 2022/7/16
# @Author  : 微信公众号：K哥爬虫
# @FileName: ggzy.py
# @Software: PyCharm
# =======================


import urllib.parse
import execjs
import requests


url = f'http://ggzy.jcs.gov.cn/website/anno/index'


def encrypted_project_id(id_enc):
    with open('ggzy_js.js', 'r', encoding='utf-8') as f:
        public_js = f.read()
        project_id = execjs.compile(public_js).call('Public', id_enc)
    return project_id


def encrypted_project_info(info_enc):
    with open('ggzy_js.js', 'r', encoding='utf-8') as f:
        public_js = f.read()
        project_info = execjs.compile(public_js).call('Public', info_enc)
    return project_info


def get_project_info(info_name, info_type):
    index_url = 'http://ggzy.jcs.gov.cn/pro-api-construction/construction/bidder/bidSection/list?pageNum=1&pageSize=20&releaseTime=&search=&informationType=%s&departmentId=&projectType=SZFJ&informationName=%s&onlyCanBidSectionFlag=NO' % (info_type, info_name)
    urlparse = urllib.parse.urlparse(index_url)
    project_info = urllib.parse.parse_qs(urlparse.query)['informationName'][0]
    return project_info


def get_content(page, info_name, info_type):
    headers = {
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "Referer": "http://ggzy.jcs.gov.cn/website/transaction/index",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    url_param = "http://ggzy.jcs.gov.cn/pro-api-construction/construction/bidder/bidSection/list"
    params = {
        "pageNum": page,
        "pageSize": "20",
        "releaseTime": "",
        "search": "",
        "informationType": info_type,
        "departmentId": "",
        "projectType": "SZFJ",
        "informationName": info_name,
        "onlyCanBidSectionFlag": "NO"
    }
    response = requests.get(url=url_param, headers=headers, params=params)

    return response


def main():
    print("""=======================================================================
                      交易信息类别: 市政、房建工程
预审/候审公告: 信息类型 ---> ZBGG   公告类型 ---> ANNOUNCEMENT
变更公告: 信息类型 ---> ZBGG   公告类型 ---> ANNOUNCEMENT_CHANGE
预审结果公示: 信息类型 ---> YSJG   公告类型 ---> ANNOUNCEMENT_YS
中标候选人公示: 信息类型 ---> ZBHXRGS   公告类型 ---> ANNOUNCEMENT_CANDIDATE
中标公示: 信息类型 ---> ZBGS   公告类型 ---> ANNOUNCEMENT_WIN
=======================================================================""")
    info_name = input("请输入信息类型:")
    info_type = input("请输入公告类型:")
    page = input("您想要获取数据的页数:")
    get_content(page, info_name, info_type)
    response = get_content(page, info_name.upper(), info_type.upper())
    num = int(page) * 20
    print("总共获取了 %d 个项目" % num)
    for i in range(20):
        title = response.json()['rows'][i]['content']
        query_id = response.json()['rows'][i]['projectId']
        query_info = get_project_info(info_name.upper(), info_type.upper())
        project_id_enc = encrypted_project_id(str(query_id))
        project_info_enc = encrypted_project_info(query_info)
        project_url = '%s?projectId=%s&projectInfo=%s' % (url, project_id_enc, project_info_enc)
        print("第 %d 个项目:" % (i+1) + "\n" + "项目名称：%s  项目编号：%d " % (title, query_id) + "\n" + "项目链接：%s" % project_url)


if __name__ == '__main__':
    main()
