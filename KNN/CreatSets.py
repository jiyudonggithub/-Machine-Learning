# -*- coding: utf-8 -*-
# @Time : 2020/9/4 20:36
# @Author : Jiyudong
# @FileName: CreatSets.py
# @Software: PyCharm

'''
创建数据集

return :
    group : 数据集
    lables : 分类标签
'''
import numpy as np


def creatSetData():
    # 四组二维数据
    group = np.array([[1, 101], [5, 89], [108, 5], [115, 8]])
    # 四组特征标签
    lables = ['爱情片', '爱情片', '动作片', '动作片']
    return group, lables


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


if __name__ == '__main__':
    # 创建数据集
    group, lables = creatSetData()
    # 打印数据集
    # print(list(zip(group.tolist(), lables)))
    # 测试数据集
    test = [101,20]
    # knn分类
    test_class = classiFication(test,group,lables,3)
    # 查看结果
    print(test_class)

