# -*- coding: utf-8 -*-
# @Time : 2019/7/19 9:27
# @Author : Jiyudong
# @FileName: ListDemo.py
# @Software: PyCharm
ss = [1, 2, 3]
ss1 = ss.extend([4, 5, 6])
ss.append([4, 5, 6])
ss2 = [("ba", 8), ("ac", 2), ("ab", 1)]
print(len(ss))
ss2.sort(key=lambda x: x[0])
print(ss2)
a = 6
if a // 3 == 0 and a != 9:
    print(a, 'dd')
else:
    print(a, 'ss')
