# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-03-28 15:35
# className:  comprehension_demo.py

# format：字符串格式化的一种方式
a = "传智{}播客".format(1)
print(a)    # 传智1播客
a1 = "传智{}播客".format([1, 2, 3])
print(a1)   # 传智[1, 2, 3]播客
a2 = "传智{}播客".format({1, 2, 3})
print(a2)   # 传智{1, 2, 3}播客
a3 = "传{}智播{}客".format({1, 2, 3}, [4, 5, 6])
print(a3)   # 传{1, 2, 3}智播[4, 5, 6]客
a4 = "传{}智播{}客".format({1, 2, 3}, 1)
print(a4)   # 传{1, 2, 3}智播1客

# 列表推导式     --帮助我们快速的生成包含一堆数据的列表
b = [i+10 for i in range(10)]
print(b)    # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

b1 = ["10月{}日".format(i) for i in range(1, 10)]
print(b1)    # ['10月1日', '10月2日', '10月3日', '10月4日', '10月5日', '10月6日', '10月7日', '10月8日', '10月9日']

# 字典推导式     --帮助我们快速的生成包含一堆数据的字典
c = {i+10:i for i in range(10)}
print(c)    # {10: 0, 11: 1, 12: 2, 13: 3, 14: 4, 15: 5, 16: 6, 17: 7, 18: 8, 19: 9}
c1 = {"a{}".format(i): 10 for i in range(3)}
print(c1)   # {'a0': 10, 'a1': 10, 'a2': 10}

# 三元运算符
# if 后面的条件成立，就把if前面的结果赋值给a，否则把else后面的结果赋值给a
d = 10 if 4 > 3 else 20
print(d)    # 10
d1 = 10 if 4 < 3 else 20
print(d1)   # 20
