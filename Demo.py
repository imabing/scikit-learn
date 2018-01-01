# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from sklearn import datasets
from sklearn import linear_model
# 346346

if __name__ == '__main__':
    iris = datasets.load_iris()
    print("The iris' target names: ", iris.target_names)
    x = iris.data
    y = iris.target

    linear = linear_model.LinearRegression()
    linear.fit(x, y)
    print("linear's score: ", linear.score(x, y))
    linear.coef_  # 系数
    linear.intercept_  # 截距
    print("predict: ", linear.predict([[7, 5, 2, 0.5], [7.5, 4, 7, 2]]))