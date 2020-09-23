# -*- coding: utf-8 -*-
# @Time : 2020/9/17 20:18
# @Author : Jiyudong
# @FileName: NBCGarberEmail.py
# @Software: PyCharm
import functools
import os
import re
import numpy as np
import random


def readDataSet(path):
    '''
    读取文件内的数据
    :param path: 文件路径
    :return: FileContent 数据集
            lableVec 数据标签
    '''
    abspath = os.path.abspath(path)
    FileContent = []
    lableVec = []
    listdir = os.listdir(path)
    for dirpath in listdir:
        dirpath = abspath + '\\' + dirpath
        if os.path.isdir(dirpath):
            dictList, lableList = readDataSet(dirpath)
            FileContent += dictList
            lableVec += lableList
        else:
            with open(dirpath, 'r') as f:
                FileContent.append(createVocabList(f.read()))
            if 'spam' in dirpath:
                lableVec.append(1)
            else:
                lableVec.append(0)
    return FileContent, lableVec


def createVocabList(fileContent):
    '''
    将读取的文本内容进行切割，并转成列表
    :param fileContent: 读取到文本的内容
    :return: wordVec 文本列表
    '''
    re_split = re.split(r'[^a-zA-Z]+', fileContent)
    wordVec = [word.lower() for word in re_split if len(word) > 2]
    return wordVec


def setOfWords2Vec(vocabList, inputSet):
    '''
    将文本与字典对比建成向量
    :param vocabList: 字典
    :param inputSet: 输入文本
    :return: Vec 文本向量
    '''
    Vec = np.zeros_like(vocabList, dtype=int).tolist()
    for word in inputSet:
        if word in vocabList:
            Vec[vocabList.index(word)] = 1
    return Vec


def trainNB0(trainMatrix, trainCategory):
    '''
    训练朴素贝叶斯模型，即计算调整因子
    :param trainMatrix:数据集
    :param trainCategory:分类的标签
    :return: p0Vect 各特征值在0类的转移概率P(w0|0)...
             p1Vect 各特征值在1类的转移概率P(w0|1)...
             pAusive 1类的概率
    '''
    trainNum = len(trainMatrix)

    numWords = len(trainMatrix[0])

    p0V = np.ones(numWords)
    p1V = np.ones(numWords)
    pAusive = sum(trainCategory) / float(trainNum)
    p0Denom = 2.0;
    p1Denom = 2.0
    for i in range(trainNum):
        if trainCategory[i] == 1:
            p1V += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0V += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = np.log(p1V / p1Denom)
    p0Vect = np.log(p0V / p0Denom)
    return p0Vect, p1Vect, pAusive


def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    '''
     进行朴素贝叶斯分类
    :param vec2Classify: 待评估向量
    :param p0Vec: 各特征值在0类的转移概率P(w0|0)...
    :param p1Vec: 各特征值在1类的转移概率P(w0|1)...
    :param pClass1: pAusive 1类的概率
    :return: 分类标签
    '''
    p1 = sum(vec2Classify * p1Vec) + np.log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + np.log(1.0 - pClass1)

    if p1 > p0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    vocab_list, lablesVec = readDataSet('email')
    wordDir = list(set(functools.reduce(lambda x, y: x + y, vocab_list)))
    DataList = list(range(50))
    random.shuffle(DataList)
    trainDataList = DataList[:40]
    testDataList = DataList[40:50]

    trainDataSet = [vocab_list[i] for i in trainDataList]
    trainLable = [lablesVec[i] for i in trainDataList]
    trainVec = []
    for words in trainDataSet:
        trainVec.append(setOfWords2Vec(wordDir, words))
    testDataSet = [vocab_list[i] for i in testDataList]
    testLable = [lablesVec[i] for i in testDataList]
    testVec = []
    for words in testDataSet:
        testVec.append(setOfWords2Vec(wordDir, words))

    nb_p0, nb_p1, nb_pA = trainNB0(trainVec, trainLable)
    testVecLable = []
    for test in testVec:
        testVecLable.append(classifyNB(test, nb_p0, nb_p1, nb_pA))
    print('测试集的分类：    ', testVecLable)
    print('测试集的真实分类：', testLable)
