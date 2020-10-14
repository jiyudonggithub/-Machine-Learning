# -*- coding: utf-8 -*-
# @Time : 2020/10/9 19:31
# @Author : Jiyudong
# @FileName: logistic1.py
# @Software: PyCharm

import numpy as np
import scipy.special
from matplotlib import pyplot as plt


def load_date(file):
    '''
    加载数据
    :param file: 数据集的位置
    :return: 数据集
    '''
    # 用np来加载数据，以\t来作为分隔符，并跳过第一行
    trainset = np.loadtxt(fname=file, delimiter='\t', skiprows=1)
    # 对矩阵的前两列进行归一化
    b = trainset[:, :2]
    mean = b.mean(axis=0)
    std = b.std(axis=0)
    c = (b - mean) / std
    trainset[:, :2] = c
    m, n = np.shape(trainset)
    # 添加一列，并换到第一列即z=w0*1 + w1x1 + w2x2
    an = np.ones((m, 1))
    cn = np.c_[trainset, an]
    trainset = cn[:, [3, 0, 1, 2]]
    return trainset


def gradAscent(Set):
    train_date = np.mat(Set[:, :3])
    train_lab = np.mat(Set[:, -1]).T
    m, n = np.shape(train_date)
    alph = 0.001
    maxCycles = 500
    weights = np.ones((n, 1))
    Jw = []
    for k in range(maxCycles):
        # Sigmoid函数
        h = scipy.special.expit(train_date * weights)
        error = train_lab - h
        # 梯度下降
        weights = weights + alph * train_date.T * error
        # 损失函数
        jw = ((train_date * weights - train_lab).T * (train_date * weights - train_lab)) / (2 * m)
        Jw.append(jw.getA())
    return weights.getA(), Jw


def drawing(Set, Fx):
    fx = list(list(zip(*Fx.tolist()))[0])
    x1 = Set[Set[:, -1] == 1][:, 1]
    y1 = Set[Set[:, -1] == 1][:, 2]
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.scatter(x=x1, y=y1, c='y', alpha=0.5)
    x2 = Set[Set[:, -1] == 0][:, 1]
    y2 = Set[Set[:, -1] == 0][:, 2]
    plt.scatter(x=x2, y=y2, c='r', alpha=0.5)
    x = np.arange(-3.0, 3.0, 0.1)
    y = (-fx[0] - fx[1] * x) / fx[2]
    plt.plot(x, y, c='b')
    plt.show()


if __name__ == '__main__':
    train_set = load_date('testSet.txt')
    q, jw = gradAscent(train_set)
    print(q)
    print(jw)
    drawing(train_set, q)
