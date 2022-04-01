# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-03-29 15:32
# className:  try_login3.py
import requests
session = requests.session()
post_url = "https://security.kaixin001.com/login/login_post.php"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"}
post_data = {"loginemail": "cqxiaoyi@163.com", "password": "wo...7529"}

"""
先发送post请求，获取cookie，带上cookie请求登录后的页面
1.session = requests.session()  # session具有的方法和requests一样
2.session.post(url, data, headers)  # 服务器设置在本地的cookie会保存在session中
3.session.get(url)  # 会带上之前保存在session中的cookie，能够请求成功
"""

session.post(post_url, headers=headers, data=post_data)
# 再使用session请求登录后的页面
url = "https://www.kaixin001.com"
response = session.get(url, headers=headers)

with open("kaixinwang2.html", "w", encoding="utf-8")as f:
    f.write(response.content.decode())