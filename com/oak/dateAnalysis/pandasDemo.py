# -*- coding: utf-8 -*-
# @Time : 2019/7/25 9:16
# @Author : Jiyudong
# @FileName: pandasDemo.py
# @Software: PyCharm
import pandas as pd
import numpy as np

# print(pd.Series([1, 2, 4, 5, 6, 7]))
# print("".center(60, "+"))
# print(pd.Series(list(range(6)), index=list('abcdef')))
# data = pd.date_range('20190101', periods=6)
# print("".center(60, "+"))
# print(data)
# print("".center(60, "+"))
# df = pd.DataFrame(np.random.randn(6, 4))
# print(df)
df = pd.read_csv(r'F:/Desktop/iris.csv')
a = df['Species']
# print(df.head(5))
print(a[:5])
a = a.astype(str)
print(a[:5])
b = a[str(a) == 'setosa']
print(b[:5])
df.replace()