"""
Write a function that uses the Jacobi method to solve a system of linear equations given by Ax = b.
The function should iterate 10 times, rounding each intermediate solution to four decimal places,
and return the approximate solution x.

The Jacobi method iteratively solves each equation for x[i] using the formula
x[i] = (1/a_ii) * (b[i] - sum(a_ij * x[j] for j != i))
where a_ii is the diagonal element of A and a_ij are the off-diagonal elements.
"""
import numpy as np


def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    result = []
    return result


if __name__ == '__main__':
    A = [[5, -2, 3],
         [-3, 9, 1],
         [2, -1, -7]]
    b = [-1, 2, 3]
    n = 2
    x = solve_jacobi(A, b, n)
    print(x)
