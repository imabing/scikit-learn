# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd

import pylab
pylab.mpl.rcParams['font.sans-serif'] = ['SimHei']
pylab.mpl.rcParams['axes.unicode_minus'] = False

if __name__ == '__main__':
    iris = pd.read_csv("iris.csv")
    col_list = ['萼长', '萼宽', '瓣长', '瓣宽', '类别']
    iris.columns = col_list
    #打印数据集
    # print(iris)
    # 数据集列统计
    # print(iris.describe())
    # 鸢尾花类别:{'versicolor', 'virginica', 'setosa'}
    classes=set(iris.loc[:,'类别'])
    # print(classes)

    #筛选setosa的数据，并作散点图
    a = iris[iris['类别'] == 'setosa']
    ax = a.plot(kind="scatter", x='萼长', y='萼宽', label='seotsa')

    # 筛选versicolor的数据，并作散点图
    b = iris[iris['类别'] == 'versicolor']
    b.plot(kind="scatter", x='萼长', y='萼宽', color='red', label='versicolor', ax=ax)

    # ＃筛选virginica的数据，并作散点图
    c = iris[iris['类别'] == 'virginica']
    c.plot(kind="scatter", x='萼长', y='萼宽', color='green', label="virginica", ax=ax)


    plt.title('三个类别萼长与萼宽分布')
    plt.legend(loc='upper right')
    plt.show()

