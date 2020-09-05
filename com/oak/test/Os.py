# -*- coding: utf-8 -*-
# @Time : 2019/7/20 10:06
# @Author : Jiyudong
# @FileName: Os.py
# @Software: PyCharm
import os
print(os.name)
# 获得环境变量
print(os.environ)
# 获得当前的工作目录
print(os.getcwd())
# 获得目录下的所有文件
print(os.listdir())
# 创建目录
# os.mkdir()
# # 删除目录
# os.rmdir()
os.system("notepad")
