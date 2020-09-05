# -*- coding: utf-8 -*-
# @Time : 2019/7/18 8:40
# @Author : Jiyudong
# @FileName: readfile.py
# @Software: PyCharm
file = open("F:/Desktop/123.txt", "a+")
# file.writelines("你好世界\n")
# file.writelines("你好中国\n")
# file.writelines("你好安徽\n")
# file.writelines("你好合肥\n")
# file.flush()
word = file.read()
print(word)
file.seek(0)
print("====".center(30, "-"))
for line in file:
    print(line, end="")
print("结束")
file.close()