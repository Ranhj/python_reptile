# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-03-29 14:19
# className:  try_login1.py
import requests

url = "https://www.kaixin001.com"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
           "Cookie": "_ref=6242ae84b504e; _cpmuid=1396404463; SERVERID=_srv80-73_; BAIDU_SSP_lcr=http://www.hao123.com/shequ/; _vid=C9C3D2C9B9A0000174551ACD5CA0DC40; Hm_lvt_500f908d39095efce74d0e9c64f55ffb=1648537222; Hm_lpvt_500f908d39095efce74d0e9c64f55ffb=1648537354; _reg_src=hao123_www_shequ; _preemail=cqxiaoyi%40163.com; _laid=0; _sso=182166021; _user=73c5945009f81f7a727c6a315f23e528_182166021_1648537378; _uid=182166021; _email=cqxiaoyi%40163.com"}



response = requests.get(url, headers=headers)
# print(response)

with open("kaixinwang1.html", "w", encoding="utf-8") as f:
    f.write(response.content.decode())