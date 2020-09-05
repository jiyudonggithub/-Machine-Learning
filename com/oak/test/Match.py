# -*- coding: utf-8 -*-
# @Time : 2019/7/20 9:23
# @Author : Jiyudong
# @FileName: Match.py
# @Software: PyCharm
def ferbonaqie(num):
    a, b, count = 0, 1, 0
    while True:
        if count > num:
            return
        yield a
        a, b = b, a + b
        count += 1
def fi(num):
    if num == 1 or num == 0:
        return 1
    else:
        return fi(num - 1) + fi(num - 2)
f = ferbonaqie(10)
c = fi(5)
print(c)
for i in f:
    print(i, end="\t")
print()
# for i in c:
#     print(i, end="\t")
