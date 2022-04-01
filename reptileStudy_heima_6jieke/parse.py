# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-03-29 11:22
# className:  parse.py
import requests
from retrying import retry

"""
专门请求url地址的方法
"""

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
           }

# headers = {
#             "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Mobile Safari/537.36",
#             "Referer": "https://www.163.com/"
# }

@retry(stop_max_attempt_number = 3)     # 让被装饰的函数反复执行三次，三次全部报错才会报错，中间有一次正常，程序继续往后走
def _parse_url(url):
    print("*"*100)
    print(url)
    response = requests.get(url, headers=headers, timeouts=5)
    return response.content.decode()

def parse_url(url):
    try:
        html_str = _parse_url(url)
    except:
        html_str = None
    return html_str


if __name__ == '__main__':
    url = "https:www.baidu.com/"
    print(parse_url(url))
