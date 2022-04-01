# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-03-29 15:58
# className:  json_demo.py
# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-03-29 10:25
# className:  try_requests_post.py
import json

import requests

url = "https://fanyi.baidu.com/v2transapi?from=zh&to=en"

query_string = input("请输入要翻译的中文:")
data = {"query": query_string,
                "from": "zh",
                "to": "en"}
print(data)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
           "Referer":  "https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh",
           "Host": "fanyi.baidu.com",
           "cookie":"BIDUPSID=EFC60A6794F3B0314B08EE8845D871ED; PSTM=1648198988; BAIDUID=EFC60A6794F3B0318B51C3D5230C2BDF:FG=1; BAIDUID_BFESS=EFC60A6794F3B0318B51C3D5230C2BDF:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_10_0_2=1; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1648520618; H_WISE_SIDS=110085_127969_179347_184716_188741_189755_190627_191068_192958_194085_195342_196428_196527_197241_197471_197711_197956_198254_199569_200993_201104_201193_201708_202544_203310_203360_203605_204100_204122_204255_204305_204427_204725_204859_204917_205218_205382_205553_205959_206007_206167_206277_206283_206515_206682_206729_206870_206905_207006_207021_207124_207178_207234_207363_207525_207552_207609_207610_207683_207729_207768_207831_207992_208000_208045_208054_208113_208162_208164_208217_208226_208267_208270_208298_208512_208718; SE_LAUNCH=5%3A27475425_0%3A27475425_16%3A27475425_15%3A27475425_31%3A27475569; PSCBD=31%3A1; H_PS_PSSID=35835_31254_34812_36166_34584_36120_36193_36032_36126_35994_35320_26350_36046_36103_36061; delPer=0; PSINO=6; BA_HECTOR=8h0g208l0421ah2h1d1h45h7i0r; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1648520408,1648542964; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1648543189; ab_sr=1.0.1_MTkzMDVkNGNjYTM4MzE1ODRmZDNjNjk1ZWMxOTE1YmFkZTcyNzg5NWE1NTlmOWFkZjFiMDczOTFhMTcyNDEzOWU1ZmNmYTVkMjM4NzI1YTY3MTQyZmM4NmFhODNmMjE0ZjJmOGI2NTUxODNmZDU3Mjk0NTdhOWU0ZDBhMGI2YjNmN2E1MDgzMjdkOWU5MzdiM2E0MDU4MjY5ZTlkMjQwOA=="}

response = requests.post(url, data=data, headers=headers)

html_str = response.content.decode()  # json 字符串
dict_ret = json.loads(html_str)

ret = dict_ret["trans"][0]["rst"]
print("翻译结果是：", ret)

# 没有获取到我想要的那一串响应，后面慢慢搞