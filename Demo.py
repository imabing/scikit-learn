# -*- coding: utf-8 -*-

import pandas as pd

if __name__ == '__main__':
    iris = pd.read_csv("iris.csv")
    col_list = ['萼长', '萼宽', '瓣长', '瓣宽', '类别']
    iris.columns = col_list
    #打印数据集
    # print(iris)
    # 数据集列统计
    print(iris.describe())
    # 鸢尾花类别:{'versicolor', 'virginica', 'setosa'}
    classes=set(iris.loc[:,'类别'])
    # print(classes)
