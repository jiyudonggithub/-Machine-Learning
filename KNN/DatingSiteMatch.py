# -*- coding: utf-8 -*-
# @Time : 2020/9/4 21:41
# @Author : Jiyudong
# @FileName: DatingSiteMatch.py
# @Software: PyCharm
from matplotlib.font_manager import FontProperties
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

'''
函数说明：读取数据集
    将数据分为特征向量和标签向量

'''


def file2Match(file):
    # 读取文本数据
    with open(file, "r") as f:
        lines = f.readlines()
    #     将每样本进行分割，并将标签用数字代替
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        lines[i] = lines[i].split("\t")
    lines = np.array(lines)
    lines = pd.DataFrame(lines)
    lines.columns = ["a", 'b', 'c', 'd']
    lines['d'][lines['d'] == 'largeDoses'] = 3
    lines['d'][lines['d'] == 'smallDoses'] = 2
    lines['d'][lines['d'] == 'didntLike'] = 1
    lables = lines["d"].tolist()
    train = lines[lines.columns[:3]].values
    train = train.astype(np.float32)
    return train, lables


"""

显示数据
    Parameter
       trainData    数据集的特征向量
       labelsData   数据集的标签向量

"""


def showDatas(trainData, labelsData):
    # 设置显示的字体和大小
    font = FontProperties(fname="汉仪雪君体.ttf", size=14)
    # 画四个图
    fig, axs = plt.subplots(nrows=2, ncols=2)
    # 将每个不同的类分成不同的颜色
    LableColors = []
    for i in labelsData:
        if i == 1:
            LableColors.append('k')
        if i == 2:
            LableColors.append('y')
        if i == 3:
            LableColors.append('r')
    axs[0][0].scatter(x=trainData[:, 0], y=trainData[:, 1], edgecolors=LableColors, s=15, alpha=0.5)
    axs0_title_text = axs[0][0].set_title("每年获得的飞行常客里程数与玩视频游戏所消耗时间占比", FontProperties=font)
    axs0_xlabel_text = axs[0][0].set_xlabel('每年获得的飞行常客里程数', FontProperties=font)
    axs0_ylabel_text = axs[0][0].set_ylabel('玩视频游戏所消耗时间占', FontProperties=font)
    plt.setp(axs0_title_text, size=9, weight='bold', color='red')
    plt.setp(axs0_xlabel_text, size=7, weight='bold', color='black')
    plt.setp(axs0_ylabel_text, size=7, weight='bold', color='black')

    axs[0][1].scatter(x=trainData[:, 0], y=trainData[:, 2], color=LableColors, s=15, alpha=.5)
    # 设置标题,x轴label,y轴label
    axs1_title_text = axs[0][1].set_title(u'每年获得的飞行常客里程数与每周消费的冰激淋公升数', FontProperties=font)
    axs1_xlabel_text = axs[0][1].set_xlabel(u'每年获得的飞行常客里程数', FontProperties=font)
    axs1_ylabel_text = axs[0][1].set_ylabel(u'每周消费的冰激淋公升数', FontProperties=font)
    plt.setp(axs1_title_text, size=9, weight='bold', color='red')
    plt.setp(axs1_xlabel_text, size=7, weight='bold', color='black')
    plt.setp(axs1_ylabel_text, size=7, weight='bold', color='black')

    # 画出散点图,以datingDataMat矩阵的第二(玩游戏)、第三列(冰激凌)数据画散点数据,散点大小为15,透明度为0.5
    axs[1][0].scatter(x=trainData[:, 1], y=trainData[:, 2], color=LableColors, s=15, alpha=.5)
    # 设置标题,x轴label,y轴label
    axs2_title_text = axs[1][0].set_title(u'玩视频游戏所消耗时间占比与每周消费的冰激淋公升数', FontProperties=font)
    axs2_xlabel_text = axs[1][0].set_xlabel(u'玩视频游戏所消耗时间占比', FontProperties=font)
    axs2_ylabel_text = axs[1][0].set_ylabel(u'每周消费的冰激淋公升数', FontProperties=font)
    plt.setp(axs2_title_text, size=9, weight='bold', color='red')
    plt.setp(axs2_xlabel_text, size=7, weight='bold', color='black')
    plt.setp(axs2_ylabel_text, size=7, weight='bold', color='black')

    didntLike = mlines.Line2D([], [], color='black', marker='.',
                              markersize=6, label='didntLike')
    smallDoses = mlines.Line2D([], [], color='orange', marker='.',
                               markersize=6, label='smallDoses')
    largeDoses = mlines.Line2D([], [], color='red', marker='.',
                               markersize=6, label='largeDoses')
    # 添加图例
    axs[0][0].legend(handles=[didntLike, smallDoses, largeDoses])
    axs[0][1].legend(handles=[didntLike, smallDoses, largeDoses])
    axs[1][0].legend(handles=[didntLike, smallDoses, largeDoses])
    # 显示图片
    plt.show()


"""
函数说明：数据标准化
    :parameter
        dataSet 数据集
    :return
        normeDataSet    标准化后的数据
        ranges          数据集的范围
        minVals         数据集的最小值
"""


def standardScaleData(dataSet):
    for i in range(dataSet.shape[1]):
        size = dataSet.shape[0]
        minVals = dataSet[:, i].min()
        maxVals = dataSet[:, i].max()
        ranges = maxVals - minVals

        dataSet[:, i] = dataSet[:, i] - minVals

        dataSet[:, i] = dataSet[:, i] / ranges
    return dataSet


'''
函数说明：KNN算法，分类器

Parameter
    test    测试集
    train   训练集
    lables  特征标签
    k       选取距离最小的K个点


Return
    sortedClassCount[0][0] - 分类结果

'''


def classiFication(test, train, lables, k=1):
    # 查看训练数据集个数
    trainSize = train.shape[0]
    # 算出测试集到已知类的距离差[(x1 -x2) , (y1-y2)]
    diffMat = np.tile(test, (trainSize, 1)) - train
    # 距离差进行平方[(x1 -x2)**2 , (y1-y2)**2]
    sqDiffMat = diffMat ** 2
    # 在将平方进行加起来(x1 -x2)**2 + (y1-y2)**2
    sqDistances = sqDiffMat.sum(axis=1)
    distance = sqDistances ** 0.5
    # 距离的降序排列的索引值
    sortDistanceIndex = distance.argsort()
    # 记录k个最小距离的类别
    classiCount = {}
    for i in range(k):
        voteIlable = lables[sortDistanceIndex[i]]
        classiCount[voteIlable] = classiCount.get(voteIlable, 0) + 1
    # 将记录的类别的个数进行排序，并返回个数最多的类别即knn的分类
    sortClassiCount = sorted(classiCount.items(), key=lambda x: x[1], reverse=True)
    return sortClassiCount[0][0]


"""
函数说明:分类器测试函数

Parameters:
    无
Returns:
    normDataSet - 归一化后的特征矩阵
    ranges - 数据范围
    minVals - 数据最小值

"""


def datingClassTest():
    # 将返回的特征矩阵和分类向量分别存储到datingDataMat和datingLabels中
    datingDataMat, datingLabels = file2Match("dataSet.txt")
    # 取所有数据的百分之十
    hoRatio = 0.10
    # 数据归一化,返回归一化后的矩阵,数据范围,数据最小值
    normMat = standardScaleData(datingDataMat)
    # 获得normMat的行数
    m = normMat.shape[0]
    # 百分之十的测试数据的个数
    numTestVecs = int(m * hoRatio)
    # 分类错误计数
    errorCount = 0.0

    for i in range(numTestVecs):
        # 前numTestVecs个数据作为测试集,后m-numTestVecs个数据作为训练集
        classifierResult = classiFication(normMat[i, :], normMat[numTestVecs:m, :],
                                          datingLabels[numTestVecs:m], 7)
        print("分类结果:%d\t真实类别:%d" % (classifierResult, datingLabels[i]))
        if classifierResult != datingLabels[i]:
            errorCount += 1.0
    print("错误率:%f%%" % (errorCount / float(numTestVecs) * 100))


'''

'''


def isSUitable():
    a = int(input("玩视频游戏所消耗时间占:"))
    b = int(input("每年获得的飞行常客里程数:"))
    c = float(input("每周消费的冰激淋公升数:"))
    datingDataMat, datingLabels = file2Match("dataSet.txt")
    suitNumber = classiFication([b, a, c], datingDataMat, datingLabels, 7)
    if suitNumber == 1:
        print("Sorry this man isnot suitbale for you ")
    elif suitNumber == 2:
        print("Congratulation this man is suitbale for you ")
    else:
        print("Your match made in heaven")



if __name__ == "__main__":
    dataFile = "dataSet.txt"
    # train, lables = file2Match(dataFile)
    # showDatas(train, lables)
    # datingClassTest(dataFile)
    isSUitable()
