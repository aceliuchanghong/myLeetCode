"""
Write a function that performs linear regression using the normal equation.
The function should take a matrix X (features) and a vector y (target) as input,
and return the coefficients(系数) of the linear regression model.
Round your answer to four decimal places, -0.0 is a valid result for rounding a very small number.

正规方程的线性回归
"""
import numpy as np


def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X = np.array(X)
    # y调整为列向量
    y = np.array(y).reshape(-1, 1)
    # Add a column of ones to X to account for the intercept term
    X_b = np.c_[np.ones((X.shape[0], 1)), X]
    print(y.shape)
    theta = []
    return theta


if __name__ == '__main__':
    X = [[1, 1],
         [1, 2],
         [1, 3]]
    y = [1, 2, 3]
    theta = linear_regression_normal_equation(X, y)
    print(theta)
