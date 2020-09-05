# -*- coding: utf-8 -*-
# @Time : 2019/7/19 9:00
# @Author : Jiyudong
# @FileName: Iterable.py
# @Software: PyCharm
from collections import Iterable
from collections import Iterator

# 判断是否可迭代
print(isinstance([], Iterable))
# 判断是否是迭代器
print(isinstance((i for i in range(5)), Iterator))

print(isinstance(iter([2, 4, 5, 8, 9, 74]), Iterator))
