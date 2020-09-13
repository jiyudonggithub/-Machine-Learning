# -*- coding: utf-8 -*-
# @Time : 2020/9/7 17:03
# @Author : Jiyudong
# @FileName: Tree01.py
# @Software: PyCharm
import math
import pandas as pd
import collections
import pickle

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
        for key, values in ADdict.items():
            adpron = values / sumNumber
            hadpron = 0.0
            # 在满足该列的某个值是的是否贷款的情况
            dd = dataFrame[dataFrame.loc[:, columsNumber] == key].iloc[:, -1]
            adsumNumber = len(dd)
            haddict = dict(collections.Counter(dd))
            for values in haddict.values():
                pron = values / adsumNumber
                hadpron -= pron * math.log(pron, 2)
            HD -= adpron * hadpron
        return HD


def calcInformationEntropy(dataset):
    '''
        函数说明：计算信息增益熵
        :param dataset: 数据集
        :return: 各特征的信息增益，信息熵
    '''
    HD = calGain(0, dataset, -1)
    adgain = []
    for i in dataset.columns.values.tolist()[:-1]:
        var = calGain(HD, dataset, i)
        adgain.append(var)
    return adgain, HD


def chooseBestFeatureSplit(dataset):
    '''
    选择最优的信息增资：分类节点
    :param dataset: 测试集数据
    :return: 最优增益的列值
    '''
    HADGain, HD = calcInformationEntropy(dataset)
    HADGainList = list(enumerate(HADGain))
    HADGainList.sort(key=lambda d: d[1], reverse=True)
    return HADGainList[0][0]


def creatTree(dataset, lables):
    '''
    创建决策树结构
    :param dataset: 测试集数据
    :param lables:  分类标签
    :return:
    '''
    ls = dict(collections.Counter(dataset.iloc[:, -1]))
    ls = sorted(ls.items(), key=lambda a: a[1], reverse=True)
    if len(ls) == 1:
        return ls[0][0]
    if dataset.shape[1] == 1:
        return ls[0][0]
    bestFeatable = chooseBestFeatureSplit(dataset)
    namebestFeatable = lables[bestFeatable]
    myTree = {namebestFeatable: {}}
    del (lables[bestFeatable])
    uniquevals = set(dataset.iloc[:, bestFeatable])
    for values in uniquevals:
        df1 = dataset[dataset.iloc[:, bestFeatable] == values]
        df1 = df1.drop(bestFeatable, axis=1)
        df1.columns = range(df1.shape[1])
        df1.index = range(df1.shape[0])
        myTree[namebestFeatable][values] = creatTree(df1, lables)
    return myTree


def classify(inputTree, lables, testset):
    '''
    样本预测分类
    :param inputTree: 数据模型
    :param labledict: 特征值向量
    :param testset:   测试集数据
    :return:
    '''
    lablesDict = dict(enumerate(lables))
    lablesDict = dict(zip(lablesDict.values(), lablesDict.keys()))
    # 获取决策树结点
    firstStr = next(iter(inputTree))
    # 下一个字典
    secondDict = inputTree[firstStr]
    featIndex = lablesDict.get(firstStr)

    for key in secondDict.keys():
        if testset[featIndex] == key:
            if type(key).__name__ == 'dict':
                classLables = classify(secondDict[key], lablesDict, testset)
            else:
                classLables = secondDict[key]
    return classLables


def storeDicsionTree(filename, inputtree):
    '''
        数据模型的存储
    :param filename: 存储文件的名称
    :param inputtree: 存储的模型
    :return:
    '''
    with open(filename, 'wb') as fw:
        pickle.dump(inputtree, fw)


def loadDicsionTree(filename):
    '''
    模型的加载
    :param filename:存储模型的文件名
    :return: 数据模型
    '''
    fr = open(filename, 'rb')
    return pickle.load(fr)


if __name__ == "__main__":
    dataSet, lables = creatDataSet()
    # HADGain, HD = calcInformationEntropy(dataSet)
    # print('信息熵为%.3f' % HD)
    # for i in range(len(HADGain)):
    #     print('第%d个特征的信息增益为：%.3f' % (i, HADGain[i]))
    # HADGainList = list(enumerate(HADGain))
    # HADGainList.sort(key=lambda d: d[1], reverse=True)

    # print('最优的特征增益是第%d个 增益为：%.3f' % (HADGainList[0][0], HADGainList[0][1]))
    testSet = [2, 0, 1, 1]
    dataSet = pd.DataFrame(dataSet)
    myTree = creatTree(dataSet, lables)
    classTable = classify(myTree, lables, testSet)
    print(classTable)
