# -*- coding: utf-8 -*-
# @Time : 2019/7/26 10:59
# @Author : Jiyudong
# @FileName: skleanDemo.py
# @Software: PyCharm
from sklearn.datasets import load_iris, fetch_20newsgroups
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier, export_graphviz


def datasets_Demo():
    '''
    数据集使用
    :return:
    '''
    iris = load_iris()
    # print("鸢尾花数据集\n", iris)
    # print("鸢尾花数据集的描述\n", iris["DESCR"])
    # print("鸢尾花数据的特征名字\n", iris.feature_names)
    # print("鸢尾花数据的特征\n", iris.data, iris.data.shape)
    x_tarin, x_test, y_tarin, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=30)
    print(x_tarin.shape)
    print(x_test.shape)
    return None


def dict_Demo():
    '''
    字典特征值提取
    :return:
    '''
    data = [{'city': '北京', 'temperature': 100}, {'city': '上海', 'temperature': 80}, {'city': '深圳', 'temperature': 90}]
    transfer = DictVectorizer(sparse=True)
    data_new = transfer.fit_transform(data)
    print(data_new)
    print(transfer.feature_names_)
    print(transfer.get_feature_names())


def count_Demo():
    '''
    文本特征抽取
    :return:
    '''
    data = ['The Editor of the Round Table has asked me to relate ',
            'some incident of my life which may be of interest to its readers. ',
            'Will they permit me to tell them that episode in my life which gives me']
    transfer = CountVectorizer()
    data_new = transfer.fit_transform(data)
    print(data_new.toarray())
    print(transfer.get_feature_names())


def knn_iris():
    '''
    使用KNN算法对鸢尾花数据分类
    :return:
    '''
    # 导数数据
    iris = load_iris()
    # 划分数据集
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=30)
    # 数据标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # knn算法训练
    estimator = KNeighborsClassifier(n_neighbors=3)
    estimator.fit(x_train, y_train)
    # 模型评估
    # 直接比较真实值和预测值
    y_predict = estimator.predict(x_test)
    print('y_predict:\n', y_predict)
    print('将真实值和预测值对比：\n', y_test == y_predict)
    # 计算准确率
    score = estimator.score(x_test, y_test)
    print('准确率为:', score)
    return None


def knn_iris_gscv():
    '''
    使用KNN算法对鸢尾花数据分类,加上网格搜索和交叉验证
    :return:
    '''
    # 导数数据
    iris = load_iris()
    # 划分数据集
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=30)
    # 数据标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # knn算法训练
    # 加上网格搜索和交叉验证
    estimator = KNeighborsClassifier()
    # 准备参数
    param_dict = {'n_neighbors': [1, 3, 5, 7, 9, 11]}
    estimator = GridSearchCV(estimator, param_grid=param_dict, cv=10)
    estimator.fit(x_train, y_train)
    # 模型评估
    # 直接比较真实值和预测值
    y_predict = estimator.predict(x_test)
    print('y_predict:\n', y_predict)
    print('将真实值和预测值对比：\n', y_test == y_predict)
    # 计算准确率
    score = estimator.score(x_test, y_test)
    print('准确率为:', score)

    # 最佳参数
    print('最佳参数', estimator.best_params_)
    # 最佳结果
    print('最佳结果', estimator.best_score_)
    # 最佳估计器
    print('最佳估计器', estimator.best_estimator_)
    # 交叉验证结果
    print('交叉验证结果', estimator.cv_results_)
    return None


def nb_news():
    '''
    用朴素贝叶斯算法对新闻进行分类
    :return:
    '''
    # 导数数据
    news = fetch_20newsgroups(subset='all')
    # 划分数据集
    x_train, x_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.3, random_state=20)
    # 特征工程：文本特征抽取-tfidf
    transfer = TfidfVectorizer()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 用朴素贝叶斯算法预估器流程
    estimator = MultinomialNB()
    estimator.fit(x_train, y_train)
    # 模型评估
    # 直接比较真实值和预测值
    y_predict = estimator.predict(x_test)
    print('y_predict:\n', y_predict)
    print('将真实值和预测值对比：\n', y_test == y_predict)
    # 计算准确率
    score = estimator.score(x_test, y_test)
    print('准确率为:', score)

    return None


def tree_iris():
    '''
    用决策树对鸢尾花进行分类
    :return:
    '''
    # 获取数据集
    iris = load_iris()
    # 数据划分:数据的特征已经抽取号可以不进行特征工程
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=30)
    # 决策树评估器
    estimator = DecisionTreeClassifier(criterion='entropy')
    estimator.fit(x_train, y_train)
    # 模型评估
    # 直接比较真实值和预测值
    y_predict = estimator.predict(x_test)
    print('y_predict:\n', y_predict)
    print('将真实值和预测值对比：\n', y_test == y_predict)
    # 计算准确率
    score = estimator.score(x_test, y_test)
    print('准确率为:', score)
    # 决策树可视化
    export_graphviz(estimator, out_file='iris_out.doc', feature_names=iris.feature_names)
    return None


if __name__ == '__main__':
    # datasets_Demo()
    # dict_Demo()
    count_Demo()
    # knn_iris()
    # knn_iris_gscv()
    # nb_news()
    #tree_iris()
