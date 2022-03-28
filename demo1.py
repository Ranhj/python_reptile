# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-03-28 9:38
# className:  demo1.py
import requests
url = 'http://www.baidu.com'
response = requests.get(url)
response.content.decode()
print(response)
print(response.request.url)
print(response.url)
print(response.headers)