# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-03-30 10:43
# className:  parse_demo.py
import requests
from retrying import retry

"""专门请求url地址的方法"""
# 模拟请求电脑端
# headers = {
#             "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
# }
# 模拟请求手机端
headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
            "Referer": "https://movie.douban.com/explore"
}


@retry(stop_max_attempt_number=3)   # 让被装饰的函数反复执行三次，三次全部报错才会报错，中间有一次正常，程序继续往后走
def _parse_url(url):
    print("*"*100)
    response = requests.get(url, headers=headers, timeout=5)
    return response.content.decode()

def parse_url(url):
    try:
        html_str = _parse_url(url)
    except:
        html_str = None
    return html_str

if __name__ == '__main__':
    # url = "http://www.baidu.com"
    url2 = "https://www.douban.com/"
    print(parse_url(url2))