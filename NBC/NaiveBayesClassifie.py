# -*- coding: utf-8 -*-
# @Time : 2020/9/14 11:13
# @Author : Jiyudong
# @FileName: NaiveBayesClassifie.py
# @Software: PyCharm
import functools
import numpy as np


def loadDataSet():
    '''

    :return: 数据集，向量标签
    '''
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],  # 切分的词条7
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],  # 8
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],  # 8
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],  # 5
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],  # 9
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]  # 6
    classVec = [0, 1, 0, 1, 0, 1]  # 类别标签向量，1代表侮辱性词汇，0代表不是
    return postingList, classVec


def setOfWoeds2Vec(vocablist, inputSet):
    '''
    将样本与本地词库做比较，并转成向量
    :param vocablist: 本地词库
    :param inputSet:  需要转换的样本
    :return: 样本向量
    '''
    returnVec = [0] * len(vocablist)
    for word in vocablist:
        if word in inputSet:
            returnVec[vocablist.index(word)] = 1
    return returnVec


def trainNB0(trainMatrix, trainCategory):
    '''
    训练朴素贝叶斯模型，即计算调整因子
    :param trainMatrix:
    :param trainCategory:
    :return:
    '''
    trainNum = len(trainMat)

    numWords = len(trainMat[0])

    p0V = np.zeros(numWords)
    p1V = np.zeros(numWords)
    pAusive = sum(trainCategory) / float(trainNum)
    p0Denom = 0.0;
    p1Denom = 0.0
    for i in range(trainNum):
        if trainCategory[i] == 1:
            p1V += trainMat[i]
            p1Denom += sum(trainMat[i])
        else:
            p0V += trainMat[i]
            p0Denom += sum(trainMat[i])
    p1Vect = p1V / p1Denom
    p0Vect = p0V / p0Denom
    return p0Vect, p1Vect, pAusive


def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    vec2Classify1 = list(filter(lambda x: x > 0, vec2Classify * p1Vec))
    vec2Classify0 = list(filter(lambda x: x > 0, vec2Classify * p0Vec))
    if len(vec2Classify0) == 0:
        return 1
    else:
        p0 = functools.reduce(lambda x, y: x * y, vec2Classify0, 1) * (1.0 - pClass1)
    if len(vec2Classify1) == 0:
        return 0
    else:
        p1 = functools.reduce(lambda x, y: x * y, vec2Classify1, 1) * pClass1
    if p1 > p0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    load_data_set, classVec_data = loadDataSet()
    vocab_list = list(set(functools.reduce(lambda x, y: x + y, load_data_set)))
    print(vocab_list)
    trainMat = []
    for data_set in load_data_set:
        trainMat.append(setOfWoeds2Vec(vocab_list, data_set))
    train_nb_p0, train_nb_p1, train_nb_pA = trainNB0(trainMat, classVec_data)
    # print('p0v:\n', train_nb_p0)
    # print('p1v:\n', train_nb_p1)
    # print('pAv:\n', train_nb_pA)
    testEntry = ['love', 'my', 'dalmation']
    ndarray = np.array(setOfWoeds2Vec(vocab_list, testEntry))
    if classifyNB(ndarray, p0Vec=train_nb_p0, p1Vec=train_nb_p1, pClass1=train_nb_pA):
        print(testEntry, '属于侮辱类')
    else:
        print(testEntry, '属于非侮辱类')
    testEntry1 = ['stupid', 'garbage']
    ndarray1 = np.array(setOfWoeds2Vec(vocab_list, testEntry1))
    if classifyNB(ndarray1, p0Vec=train_nb_p0, p1Vec=train_nb_p1, pClass1=train_nb_pA):
        print(testEntry1, '属于侮辱类')
    else:
        print(testEntry1, '属于非侮辱类')
