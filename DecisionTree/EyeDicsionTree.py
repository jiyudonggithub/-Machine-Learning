# -*- coding: utf-8 -*-
# @Time : 2020/9/11 15:58
# @Author : Jiyudong
# @FileName: EyeDicsionTree.py
# @Software: PyCharm

import pandas as pd
import pydotplus
from sklearn.preprocessing import LabelEncoder
from sklearn.externals.six import StringIO
from sklearn import tree
import os

os.environ["PATH"] += os.pathsep + r'D:\Graphviz 2.44.1\bin'

def readDataSet(filename):
    '''
    读取数据集
    :param filename: 数据文档位置
    :return: 数据集
    '''
    with open(filename, 'r') as fr:
        dataset = fr.readlines()
    for i in range(len(dataset)):
        dataset[i] = dataset[i].strip().split('\t')
    return pd.DataFrame(dataset)


if __name__ == '__main__':
    dataFile = 'lenses.txt'
    df = readDataSet(dataFile)
    className = list(set(df.iloc[:, -1]))
    le = LabelEncoder()
    for col in df.columns:
        df[col] = le.fit_transform(df[col])
    clf = tree.DecisionTreeClassifier(max_depth=4)
    lables = df.iloc[:, -1].tolist()
    trains = df.iloc[:, :-1].values.tolist()
    print('====================')
    clf = clf.fit(trains, lables)
    dot_data = StringIO()
    tree.export_graphviz(clf, out_file=dot_data, feature_names=['age', 'prescript', 'astigmatic', 'tearRate'],
                         class_names=className, filled=True, rounded=True, special_characters=True
                         )
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    graph.write_pdf('tree.pdf')
