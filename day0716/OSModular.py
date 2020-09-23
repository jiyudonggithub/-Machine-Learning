# -*- coding: utf-8 -*-
# @Time : 2020/9/13 15:26
# @Author : Jiyudong
# @FileName: OSModular.py
# @Software: PyCharm
import functools
import numpy as np

ls = ['c', 'x', 'c', 'd', 'd', 's', 's', 'e']
ls3 = np.zeros_like(ls,dtype=int)
ls4 = ls3.tolist()
print(ls4)
# fun_reduce = functools.reduce(lambda x, y: x + y, ls)
# print(fun_reduce)
# str1 = 'dsdsfds'
# str2 = 'ABVC'
# str3 = str1 + ',' + str2
# print(str3)
# trainDataSet = list[range(50)]
# print(trainDataSet)
