"""
Write a function that calculates the covariance matrix from a list of vectors.
Assume that the input list represents a dataset where each vector is a feature,
and vectors are of equal length.

1.方差是用来衡量单个变量自身变异大小的总体参数
2.协方差是用来衡量两个变量之间协同变异大小的总体参数

是一种用来衡量两个随机变量关系的统计量。
只能处理二维问题,计算协方差需要计算均值
"""

import numpy as np


def calculate_covariance_matrix2(vectors):
    """此函数有误"""
    data = np.array(vectors)
    # 留着主要是想看具体实现+这种设计模式
    data_T = data.T
    covariance_matrix = np.cov(data_T)
    return covariance_matrix


def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    n_features = len(vectors)
    n_observations = len(vectors[0])
    covariance_matrix = [[0 for _ in range(n_features)] for _ in range(n_features)]

    means = [sum(features) / n_observations for features in vectors]
    for i in range(n_features):
        for j in range(i, n_features):
            covariance = sum((vectors[i][k] - means[i]) * (vectors[j][k] - means[j]) for k in range(n_observations)) / (
                    n_observations - 1)
            covariance_matrix[i][j] = covariance_matrix[j][i] = covariance

    return covariance_matrix


if __name__ == '__main__':
    vectors = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
    covariance_matrix = calculate_covariance_matrix(vectors)
    print(covariance_matrix)
