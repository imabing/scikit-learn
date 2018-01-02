# -*- coding: utf-8 -*-
import pandas as pd
from sklearn import linear_model
from sklearn import datasets
if __name__ == '__main__':
    iris = datasets.load_iris()
    #print(iris)
    #数据
    x = iris.data
    #标签 0,1,2 代表三个类别
    y = iris.target
    #====================线性回归=======================
    linear = linear_model.LinearRegression()
    linear.fit(x, y)
    print("linear's score: ", linear.score(x, y))
    linear.coef_  # 系数
    linear.intercept_  # 截距
    print("predict: ", linear.predict([[7, 5, 2, 0.5], [7.5, 4, 7, 2]]))
    # ====================逻辑回归=======================
    logistic = linear_model.LogisticRegression()
    # logistic.predict()
    # print("predict: ", logistic.predict([[7, 5, 2, 0.5], [7.5, 4, 7, 2]]))