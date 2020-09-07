# -*- coding: utf-8 -*-
# @Time : 2020/9/7 9:09
# @Author : Jiyudong
# @FileName: DigitalIdentify.py
# @Software: PyCharm
import os

import numpy as np
from sklearn.neighbors import KNeighborsClassifier

"""
函数说明:将32x32的二进制图像转换为1x1024向量。

Parameters:
    filename - 文件名
Returns:
    returnVect - 返回的二进制图像的1x1024向量
"""


def imgToVector(filename):
    with open(filename, "r") as f:
        linestr = f.readlines()
    linestr = list(map(lambda x: x.strip(), linestr))
    linestr = "".join(linestr)
    linestr = list(linestr)
    returnVect = np.zeros((1, 1024))
    returnVect[0, :] = linestr
    return returnVect


def classiDigitalFication(TrainPath, TestPath):
    # 存储分类标签
    LablesDig = []
    # 打开训练集目录
    trainsDir = os.listdir(TrainPath)
    m = len(trainsDir)
    # 建立一个m*1024的特征向量
    trainsMat = np.zeros((m, 1024))
    for i in range(m):
        # 获取一个样本
        filestr = trainsDir[i]
        # 获取该样本的标签
        LablesDig.append(int(filestr.split('_')[0]))
        # 将文件转成向量
        trainsMat[i, :] = imgToVector(TrainPath + '/' + filestr)
    # 使用KNN算法进行训练模型
    knn = KNeighborsClassifier(n_neighbors=3, algorithm='auto')
    knn.fit(trainsMat, LablesDig)

    testDir = os.listdir(TestPath)

    NumberTest = len(testDir)
    errorCount = 0.0

    for i in range(NumberTest):
        fileNume = testDir[i]
        # 获取将测试标签
        classNumber = int(fileNume.split('_')[0])
        vectorTest = imgToVector(TestPath + '/' + fileNume)
        # 将模型预测的结果存储起来
        classPredict = knn.predict(vectorTest)
        print('KNN 分类结果%d\t 真实结果%d' % (classPredict, classNumber))
        if classPredict != classNumber:
            errorCount += 1.0
    print("总共错了%d个数据\n错误率为%f%%" % (errorCount, errorCount / NumberTest * 100))


if __name__ == '__main__':
    trainPath = 'trainingDigits'
    testPath = 'testDigits'
    classiDigitalFication(trainPath, testPath)
