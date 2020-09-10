# -*- coding: utf-8 -*-
# @Time : 2020/9/7 17:03
# @Author : Jiyudong
# @FileName: Tree01.py
# @Software: PyCharm
import math
import pandas as pd
import collections

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


def calGain(HD, dataFrame, columsNumber):
    '''
    函数说明：计算信息增益
    :param HD: 信息的熵，第一次计算要设 HD = 0
    :param dataFrame: 数据集
    :param columsNumber: 需要计算的列数
    :return:
    '''
    # 计算样本个数
    sumNumber = len(dataFrame)
    # 第一次计算需要先算出信息的熵
    if HD == 0:
        # 统计总共几种类型并出现几次
        HDdict = dict(collections.Counter(dataFrame.iloc[:, columsNumber]))
        Hd = 0.0
        for values in HDdict.values():
            pron = values / sumNumber
            Hd -= pron * math.log(pron, 2)
        return Hd
    else:
        ADdict = dict(collections.Counter(dataFrame.iloc[:, columsNumber]))
        print(ADdict)
        for key, values in ADdict.items():
            adpron = values / sumNumber
            hadpron = 0.0
            # 在满足该列的某个值是的是否贷款的情况
            dd = dataFrame[dataFrame.loc[:, columsNumber] == key].iloc[:, -1]
            adsumNumber = len(dd)
            haddict = dict(collections.Counter(dd))
            print(haddict)
            for values in haddict.values():
                pron = values / adsumNumber
                hadpron -= pron * math.log(pron, 2)
            HD -= adpron * hadpron
        return HD


'''
    函数说明：计算信息增益熵
    :param dataset: 数据集
    :return:
'''


def calcInformationEntropy(dataset):
    df = pd.DataFrame(dataset)
    HD = calGain(0, df, -1)
    adgain = []
    for i in df.columns.values.tolist()[:-1]:
        var = calGain(HD, df, i)
        adgain.append(var)
    return adgain, HD


if __name__ == "__main__":
    dataSet, lables = creatDataSet()
    HADGain, HD = calcInformationEntropy(dataSet)
    print('信息熵为%.3f' % HD)
    for i in range(len(HADGain)):
        print('第%d个特征的信息增益为：%.3f' % (i, HADGain[i]))
    HADGainList = list(enumerate(HADGain))
    HADGainList.sort(key=lambda d: d[1], reverse=True)
    print('最优的特征增益是第%d个 增益为：%.3f' % (HADGainList[0][0], HADGainList[0][1]))
