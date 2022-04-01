# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-03-29 9:54
# className:  try_requests.py
import requests

# url = "https://www.baidu.com"

url = "https://fanyi.baidu.com/basetrans"
headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Mobile Safari/537.36",
           "Referer": "https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh"}

response = requests.get(url, headers=headers)

# 获取网页的html的字符串
response.encoding = "utf-8"

# print(response)
# print(response.text)

# 把响应的二进制字节流转化为str类型
print(response.content.decode())