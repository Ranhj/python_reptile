#!/usr/bin/env python
# -*_ coding:utf-8 _*_
# author:    冉海军
# datetime:  0031  :  2022/3/31 18:25
# 文件名称:    xpath_demo.py
# IDE:       PyCharm
"""
1.选择节点(标签)：
/html/head/meta: 能够选中html下的head下的所有meta标签

2."//"：能够从任意节点开始选择
"//li"：当前页面上的所有的li标签
"/html/head/link"：head下的所有的link标签

3.@符号的用途
--选择具体某个元素：//div[@class='feed-infinite-wrapper']/ul/li  选择class='feed-infinite-wrapper'的div下的ul下的li
--a/@href：选择a的href的值

4.获取文本：
--/a/text(): 获取a下的文本
--/a//text(): 获取a下的所有的文本

5.当前
--"./a"：当前节点下的a标签
"""
from lxml import etree
import requests

url = "https://movie.douban.com/cinema/nowplaying/chongqing/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"}
response = requests.get(url, headers=headers)
html_str = response.content.decode()
print(html_str)

# 使用etree处理数据
html = etree.HTML(html_str)
print(html)

# 1.获取所有电影的url地址
url_list = html.xpath("//div[@class='indent']/div/table//div[@class='pl2]/a/@href")
print(url_list)

# 2.获取所有图片的地址
img_list = html.xpath("//div[@class='indent'/div/table//a[@class='nbg']/img/@src")
print(img_list)

# 3.需要把每部电影组成一个字典，字典中是电影的重要数据，如果标题，url，图片地址，评论数，评分
# 思路：
    # 1.分组
    # 2.每一组提取数据

ret1 = html.xpath("//div[@class='indent']/div/table")
print(ret1)

for table in ret1:
    item = {}
    item["title"] = table.xpath("./div[@class='pl2']/a//text()")[0].replace("/", "").strip()
    item["href"] = table.xpath(".//div[@class='pl2']/a/@href")[0]
    item["img"] = table.xpath(".//a[@class='nbg']/img/@src")[0]
    item["comment_num"] = table.xpath(".//span[@class='pl]/text()")[0]
    item["rating_num"] = table.xpath(".//span[@class='rating_nums']/text()")[0]
    print(item)
