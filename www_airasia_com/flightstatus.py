# ==================================
# --*-- coding: utf-8 --*--
# @Time    : 2021-10-15
# @Author  : 微信公众号：K哥爬虫
# @FileName: flightstatus.py
# @Software: PyCharm
# ==================================


import requests


status_url = 'https://k.apiairasia.com/flightstatus/status/od/v3/'


def get_flight_status(departure, destination, date):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJMQ0FLaWhpbUxlTjZ3a1FYU2FhRTgyZTh0ZDUwM3NZUiIsImlhdCI6MTUzMzY5NzU5NSwiZXhwIjoxODQ5MzE2Nzk1LCJhdWQiOiJGbGlnaHQgU3RhdHVzIiwic3ViIjoiRmxpZ2h0IFN0YXR1cyJ9._M8lPMqvBYW20NcjeUyb0iQRrUYSjIWhGwJeDY4Apns'
    }
    complete_url = status_url + departure + '/' + destination + '/' + date
    response = requests.get(url=complete_url, headers=headers)
    print(response.text)


if __name__ == '__main__':
    departure = input('请输入出发地代码：')
    destination = input('请输入目的地代码：')
    date = input('请输入日期（例如：29/09/2021）：')

    # departure = 'MFM'
    # destination = 'KUL'
    # date = '29/09/2021'
    get_flight_status(departure, destination, date)
