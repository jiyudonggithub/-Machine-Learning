#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   sensor.py    
@Contact :   yudong.j@icloud.com


@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/15 上午10:01   yudong      1.0         None
'''

import numpy as np
import matplotlib.pyplot as plt
'''
    感知机模型
'''

def getSensor(dateset):
    x_train = np.insert(dateset, 2, 1, axis=1)[:, :3]
    y_train = dateset[:, -1]
    w_train = np.ones(3)
    m, n = np.shape(x_train)
    while True:
        w_old = w_train.tolist()
        for i in range(m):
            if y_train[i] == -1:
                Xi = -x_train[i]
            else:
                Xi = x_train[i]
            if np.dot(w_train, Xi) < 0:
                w_train += Xi
        if w_old == w_train.tolist():
            break
    return w_train


def showDate(dataset, w):
    x1 = dataset[dataset[:, -1] == 1][:, 0]
    y1 = dataset[dataset[:, -1] == 1][:, 1]
    x2 = dataset[dataset[:, -1] == -1][:, 0]
    y2 = dataset[dataset[:, -1] == -1][:, 1]
    plt.scatter(x=x1, y=y1, c='y', alpha=0.5)
    plt.scatter(x=x2, y=y2, c='r', alpha=0.5)
    x = np.arange(min(dataset[:, 0]), max(dataset[:, 0]), 0.1)
    y = (-w[2] - w[0] * x) / w[1]
    plt.plot(x, y, c='b')
    plt.show()


if __name__ == '__main__':
    loadtxt = np.loadtxt(fname='/home/yudong/date.txt', delimiter='\t')
    w = getSensor(loadtxt)
    showDate(loadtxt, w)
