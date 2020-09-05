# -*- coding: utf-8 -*-
# @Time : 2019/7/19 10:09
# @Author : Jiyudong
# @FileName: Function.py
# @Software: PyCharm
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
tuple3 = tuple1 + tuple2
print(tuple3)


# num = int(input("请输入一个数："))
# print(8 / 2)
# for i in range(2, num + 1):
#     if num % i == 0:
#         if i != num:
#             print(i, "*", num // i, "=", num)
#             print("不是一个质数")
#             break
#         else:
#             print(i, 'a')
#             print("是一个质数")
def sumarr(*args):
    sun = 0
    for i in args:
        sun += i
    return sun


def num3(nums):
    sum = 0
    for i in range(nums + 1):
        sum += i ** 3
    return sum


def poup(args):
    for i in range(len(args) - 1, 0, -1):
        for j in range(0, i):
            if args[j] > args[j + 1]:
                args[j + 1], args[j] = args[j], args[j + 1]
    return args


s = [1, 8, 10, 5, 3, 4, 9, 56]


def sss(args):
    for j in range(1, len(args)):
        if args[0] < args[j]:
            a = args[j]
            args.pop(j)
            args.insert(0, a)
        else:
            i = 1
            while (i <= j):
                if args[i] < args[j]:
                    a = args[j]
                    args.pop(j)
                    args.insert(i, a)
                i += 1
    return args


def sss1(args):
    for j in range(1, len(args)):
        for i in range(j):
            if args[i] > args[j]:
                a = args[j]
                args.pop(j)
                args.insert(i, a)
                break
    return args

# print(sumarr(1, 5, 6, 7, 8, 9, 10))
# print(num3(2))
# print(poup(s))
# print("{:b}".format(-61))
print(sss(s))
print(sss1(s))
