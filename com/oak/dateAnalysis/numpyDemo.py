# -*- coding: utf-8 -*-
# @Time : 2019/7/25 8:28
# @Author : Jiyudong
# @FileName: numpyDemo.py
# @Software: PyCharm
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
print(a)
a = a.astype(float)
print(a)
a = np.zeros(6, dtype=int)
print(a)
a = np.random.randn(2, 2, 2)
print(a.shape)
# 维度
print(a.ndim)
print(a)
a = np.random.randint(1, 10, 10)
print(a)
b = a > 5
c = np.where(a > 5)
print(b)
print(c)
a = np.arange(6)
print(a)
print(a.shape)
a.shape = (6, 1)
a.T
print(a)
print(a.shape)
a = np.array([[0, 1, 2, 3, 4, 5], [10, 11, 12, 13, 14, 15]])
print(a)
b = np.array([[50, 51, 52, 53, 54, 55], [60, 61, 62, 63, 64, 65]])
b.s
print(b)
print("".center(30, '+'))
c = np.concatenate((a, b), axis=1)
print(c)
print("".center(30, '+'))
c = np.concatenate((a, b), axis=0)
print(c)
print("".center(30, '+'))
print(np.vstack((a, b)))
print("".center(30, '+'))
print(np.hstack((a, b)))
print("".center(30, '+'))
print(np.linspace(1, 20, 50))
a = np.array(['a', 'b', 'c'])
print(a.dtype)
