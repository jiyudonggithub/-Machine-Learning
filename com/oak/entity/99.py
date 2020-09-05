# -*- coding: utf-8 -*-
# @Time : 2019/7/18 16:46
# @Author : Jiyudong
# @FileName: 99.py
# @Software: PyCharm
import random

for i in range(1, 10):
    for j in range(1, i + 1):
        # print(i, "*", j, "=", i * j, end="\t")
        print("{0}*{1}={2}".format(i, j, i * j), end="\t")
    print()
print(range(1, 6))
print(random.randrange(10))
