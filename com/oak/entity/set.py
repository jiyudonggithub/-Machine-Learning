# -*- coding: utf-8 -*-
# @Time : 2019/7/18 15:53
# @Author : Jiyudong
# @FileName: set.py
# @Software: PyCharm
s1 = set([1, 2, 3, 5])
# s1.add([4, 5, 6])
# s1.update({4, 8, 9, 74})
# s.remove(89)
s1.discard(100)
print(89 in s1)
print(s1)
s2 = set([2, 3, 4, 5, 89])
# print(s2 & s1)
# print(s2 ^ s1)
# print(s2 | s1)
# print(s2 - s1)
ss2 = (1, 2, 3, 4, 5, [4, 5, 9])
print(ss2)
ss2[5][1] = 100
print(ss2)
