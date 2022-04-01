# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-03-29 17:04
# className:  try_json.py
import json
import requests

url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=1"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
           "Referer": "https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action="}
response = requests.get(url, headers=headers)
response.encoding = "utf-8"
print(response.content.decode())

json_str = response.content.decode()

# 把json字符串转化为python类型   json.loads(json字符串)
ret1 = json.loads(json_str)
print(ret1)

# json.dumps：把python类型转化为json字符串  json.dumps({})
with open("douban.txt", "w", encoding="utf-8") as f:
    f.write(json.dumps(ret1, ensure_ascii=False, indent=2))
    # ensure——ascii=False:让中文显示中文
    # indent=2:下一行在上一行的基础上退两格
