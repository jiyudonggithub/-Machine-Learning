# -*- coding: utf-8 -*-
# @Time : 2019/7/16 16:30
# @Author : Jiyudong
# @FileName: word.py
# @Software: PyCharm
import jieba

f = open("F:/Desktop/123.csv", "a+")
# word = f.read()
# ss = jieba.lcut(word)
# d = {}
# for i in ss:
#     d[i] = d.get(i, 0) + 1
# items = list(d.items())
# items.sort(key=lambda x: x[1], reverse=True)
# for i in range(10):
#     word, count = items[i]
#     print("{0:<10}{1:>5}".format(word, count))
ss = {"name": "李四", "age": 18, "tel": 1895446214}
f.write("name,age,tel")
f.close()
