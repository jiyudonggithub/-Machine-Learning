# -*- coding: utf-8 -*-
# @Time : 2020/9/3 19:28
# @Author : Jiyudong
# @FileName: DecoratorDemo.py
# @Software: PyCharm

'''
    装饰器就是一个闭包，本质上是一个返回函数的函数
'''


# 简单的装饰器

def outer(func):
    def inner(age):
        if age < 0:
            age = 0
        func(age)

    return inner
@outer
def say(age):
    print("sunck is %d years old" %(age))

say(-10)
