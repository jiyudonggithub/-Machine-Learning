#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   smo.py    
@Contact :   yudong.j@icloud.com


@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/14 上午9:51   yudong      1.0         None
'''
import numpy as np
import matplotlib.pyplot as plt
import random


def showClassifer(loadtxt, w, b, alphas):
    plt.scatter(x=loadtxt[loadtxt[:, -1] == 1][:, 0], y=loadtxt[loadtxt[:, -1] == 1][:, 1], c='y', alpha=0.5)
    plt.scatter(x=loadtxt[loadtxt[:, -1] == -1][:, 0], y=loadtxt[loadtxt[:, -1] == -1][:, 1], c='r', alpha=0.5)
    x = np.arange(-2.0, 10, 0.1)
    a1, a2 = w
    b = float(b)
    a1 = float(a1)
    a2 = float(a2)
    y = (-b - a1 * x) / a2
    plt.plot(x, y)
    for i, alpha in enumerate(alphas):
        if abs(alpha) > 0:
            x, y = loadtxt[:, :2][i]
            plt.scatter([x], [y], s=150, c='none', alpha=0.7, linewidth=1.5, edgecolor='red')
    plt.show()


def selectJrand(i, m):
    j = i
    while j == i:
        j = int(random.uniform(0, m))
    return j


def clipAlpha(aj, H, L):
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj


def smoSimple(dataset, classLabel, C, toler, maxIter):
    x_mat = np.mat(dataset)
    y_mat = np.mat(classLabel).T
    m, n = np.shape(dataset)
    alphas = np.mat(np.zeros((m, 1)))
    b = 0
    iter_num = 0
    while iter_num < maxIter:
        alphaPairsChanged = 0
        for i in range(m):
            gxi = float(np.multiply(alphas, y_mat).T * x_mat * x_mat[i].T) + b
            Ei = gxi - float(y_mat[i])
            if ((y_mat[i] * Ei < -toler) and (alphas[i] < C)) or ((y_mat[i] * Ei > toler) and (alphas[i] > 0)):
                j = selectJrand(i, m)
                gxj = float(np.multiply(alphas, y_mat).T * x_mat * x_mat[j].T) + b
                Ej = gxj - float(y_mat[j])
                alphaIold = alphas[i].copy();
                alphaJold = alphas[j].copy();
                if y_mat[i] != y_mat[j]:
                    L = max(0, alphas[j] - alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    L = max(0, alphas[j] + alphas[i] - C)
                    H = min(C, alphas[j] + alphas[i])
                eta = x_mat[i] * (x_mat[i] - x_mat[j]).T - (x_mat[i] - x_mat[j]) * x_mat[j].T
                alphas[j] += float(y_mat[j]) * (Ei - Ej) / eta
                alphas[j] = clipAlpha(alphas[j], H, L)
                alphas[i] += y_mat[j] * y_mat[i] * (alphaJold - alphas[j])
                b1 = b - Ei - y_mat[i] * x_mat[i] * x_mat[i].T * (alphas[i] - alphaIold) - y_mat[j] * x_mat[i] * x_mat[
                    j].T * (alphas[j] - alphaJold)
                b2 = b - Ej - y_mat[i] * x_mat[j] * x_mat[i].T * (alphas[i] - alphaIold) - y_mat[j] * x_mat[j] * x_mat[
                    j].T * (alphas[j] - alphaJold)
                if 0 < alphas[i] < C:
                    b = b1
                elif 0 < alphas[j] < C:
                    b = b2
                else:
                    b = (b1 + b2) / 2.0
                alphaPairsChanged += 1
        if alphaPairsChanged == 0:
            iter_num += 1
        else:
            iter_num = 0
    return b, alphas


def get_w(dataset, classLabel, alphas):
    x_mat = np.mat(dataset)
    y_mat = np.mat(classLabel).T
    w = np.multiply(alphas, y_mat).T * x_mat
    return w.tolist()[0]


def lineHard(dateset):
    m, n = dateset.shape
    dateset = np.insert(dateset, 0, np.ones(n, 1), axis=1)


if __name__ == '__main__':
    loadtxt = np.loadtxt(fname='/home/yudong/date.txt', delimiter='\t')
    x_train = loadtxt[:, :2]
    y_train = loadtxt[:, -1]
    b, alphas = smoSimple(x_train, y_train, 0.6, 0.001, 40)
    w = get_w(x_train, y_train, alphas)
    showClassifer(loadtxt, w, b, alphas)
