# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-03-29 17:40
# className:  douban_spider.py
import json
from parse_demo import parse_url
class DoubanSpider:

    def __init__(self):
        self.temp_url = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?os=android&for_mobile=1&start=0&count=18&loc_id=108288&_=1648603796009"

    def get_contentf_list(self, html_str):  # 提取数据
        dict_data = json.loads(html_str)
        content_list = dict_data["subject_collection_items"]
        total = dict_data["total"]
        return content_list, total

    def save_content_list(self, content_list):
        with open("douban2.json", "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")
        print("保存成功！！！！！！！！！！！！！！！")

    def run(self):  # 实现主要逻辑
        num = 0
        total = 100
        while num < total+18:
            # 1.start_url
            url = self.temp_url.format(num)
            print(url)
            # 2.发送请求，获取响应
            html_str = parse_url(url)
            # 3.提取数据
            content_list, total = self.get_contentf_list(html_str)
            # 4.保存
            self.save_content_list(content_list)
            # 5.构造下一页的url地址，循环2-5步
            num += 18


if __name__ == '__main__':
    douban = DoubanSpider()
    douban.run()
