# -*- coding: utf-8 -*-
# @Time : 2020/9/4 21:15
# @Author : Jiyudong
# @FileName: Demo.py
# @Software: PyCharm

# dir = {'爱情片': 6, '动作片': 3, '喜剧片': 10, '恐怖片': 9}
# dir1 = sorted(dir.items(),key=lambda x:x[1],reverse=True)
# print(dir1)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # with open("F://Desktop//dataSet.txt", "r") as f:
    #     lines = f.readlines()
    # for i in range(len(lines)):
    #     lines[i] = lines[i].strip()
    #     lines[i] = lines[i].split("\t")
    # lines = np.array(lines)
    # lines = pd.DataFrame(lines)
    # lines.columns = ["a", 'b', 'c', 'd']
    # lines['d'][lines['d'] == 'largeDoses'] = 3
    # lines['d'][lines['d'] == 'smallDoses'] = 2
    # lines['d'][lines['d'] == 'didntLike'] = 1
    # lables = lines["d"].tolist()
    # train = lines[lines.columns[:3]].values
    # LableColors = []
    # for i in lables:
    #     if i == 1:
    #         LableColors.append('k')
    #     if i == 2:
    #         LableColors.append('y')
    #     if i == 3:
    #         LableColors.append('r')
    # plt.scatter(x=train[:, 0], y=train[:, 1],
    #             c=LableColors, alpha=0.5)
    # plt.show()
    # a = {'a': '1', 'b': '2', 'c': '3'}
    #
    # for key, values in a.items():
    #     print(key + ':' + values)
    # ls = a.iteritems()
    # print(ls)
    # a = [10, 8, 56, 49, 32, 1, 5, 6, 7, 8, 9]
    # b = enumerate(a)
    # c = list(b)
    # c.sort(key=lambda d: d[1], reverse=True)
    # print(c)
    # print('=============')
    # labels = ['年龄', '有工作', '有自己的房子', '信贷情况']
    # del(labels['有自己的房子'])
    # print(labels)
    a = set([1, 2, 1, 5, 6, 2])
    for p in a:
        print(p)
