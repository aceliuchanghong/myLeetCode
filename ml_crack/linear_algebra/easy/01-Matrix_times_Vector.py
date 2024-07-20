"""
Write a function that takes the dot product of a matrix and a vector.
return -1 if the matrix could not be dotted with the vector
"""


def matrix_dot_vector(
        matrix: list[list[int | float]], vector: list[int | float]
) -> list[int | float]:
    if len(matrix[0]) != len(vector) or len(matrix) == 0 or len(vector) == 0:
        return [-1]
    result = []
    for i in range(len(matrix)):
        hold = 0
        for j in range(len(matrix[i])):
            hold += matrix[i][j] * vector[j]
        result.append(hold)
    return result


if __name__ == '__main__':
    a = [[1, 2],
         [2, 4]]
    b = [1, 2]
    c = matrix_dot_vector(a, b)
    print(c)
