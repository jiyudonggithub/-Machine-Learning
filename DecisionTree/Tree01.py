# -*- coding: utf-8 -*-
# @Time : 2020/9/7 17:03
# @Author : Jiyudong
# @FileName: Tree01.py
# @Software: PyCharm
import math

"""
创建数据集

"""


def creatDataSet():
    # 数据集
    dataSet = [[0, 0, 0, 0, 'no'],
               [0, 0, 0, 1, 'no'],
               [0, 1, 0, 1, 'yes'],
               [0, 1, 1, 0, 'yes'],
               [0, 0, 0, 0, 'no'],
               [1, 0, 0, 0, 'no'],
               [1, 0, 0, 1, 'no'],
               [1, 1, 1, 1, 'yes'],
               [1, 0, 1, 2, 'yes'],
               [1, 0, 1, 2, 'yes'],
               [2, 0, 1, 2, 'yes'],
               [2, 0, 1, 1, 'yes'],
               [2, 1, 0, 1, 'yes'],
               [2, 1, 0, 2, 'yes'],
               [2, 0, 0, 0, 'no']]
    # 分类属性
    labels = ['年龄', '有工作', '有自己的房子', '信贷情况']
    return dataSet, labels
'''
    函数说明：计算信息增益熵
    :param dataset: 数据集
    :return:
'''
def calcInformationEntropy(dataset):
    numberSample = len(dataset)
    lablesCount = {}
    for i in range(numberSample):
        print("")





if __name__ == "__main__":
    print("   ")
