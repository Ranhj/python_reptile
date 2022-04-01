# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-03-29 10:25
# className:  try_requests_post.py
import requests

url = "https://fanyi.baidu.com/basetrans"

query_string = {"query": "你好，python",
        "from": "zh",
        "to": "en"}

headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Mobile Safari/537.36",
           "Referer": "https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh"}


response = requests.post(url, data=query_string, headers=headers)
response.encoding = "utf-8"
print(response)

# 获取网页源码的正确打开方式(通过下面三种方式一定能够获取到网页的正确解码之后的字符串)

# 第一种：把响应的二进制字节流转化为str类型
print(response.content.decode())
# # 第二种：指定解码方式
# print(response.content.decode("gbk"))
# # 第三种：该方式往往会出现乱码，出现乱码就使用response.encoding="utf-8"
# print(response.text)
