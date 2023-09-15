import numpy as np


def genIt(width, length, max_value):
    res = []
    for i in range(length):
        row = []
        for j in range(width):
            num = np.random.randint(0, max_value)
            row.append(num)
        res.append(row)
    return res
