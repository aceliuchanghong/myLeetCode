# 两个有序数组A和B，分别拥有m和n的长度，求其合并后的第k个值
from fromBook.util import generateArray as ga

m, n, k = 15, 12, 20
m, n, k = 1, 2, 2
dataA = ga.newArray.generateit(m)
dataB = ga.newArray.generateit(n)

dataA.sort()
dataB.sort()
dataA, dataB = [0], [1, 2]
dataA, dataB = [1, 2], [0]


# 自己写的,错误的,我打算先找到data1里面的加data2的得到k-1一个数据,然后再找第k,有问题
def solution2(data1, data2, k):
    if k > len(data1) + len(data2) or k <= 0 or int(k) != k:
        return "k is unacceptable"
    i, j, token = 0, 0, 0
    res = []
    while i + j <= k - 2:
        if data1[i] <= data2[j]:
            res.append(data1[i])
            i += 1
            token = 0
            if i > len(data1) - 1:
                i -= 1
                j += 1
                token = 1
        else:
            res.append(data2[j])
            j += 1
            token = 0
            if j > len(data2) - 1:
                j -= 1
                i += 1
                token = 2
    if i > len(data1) - 1:
        res.append(data2[j])
    elif j > len(data2) - 1:
        res.append(data1[i])
    elif token == 1:
        res.append(data2[j])
    elif token == 2:
        res.append(data1[i])
    else:
        res.append(min(data1[i], data2[j]))
    return res


def solution(data1, data2, k):
    m, n = len(data1), len(data2)
    if m > n:
        return solution(data2, data1, k)
    left, right = 0, m
    while left < right:
        mid = (right + left) / 2
        j = k - 1 - mid
        if j >= n or data1[mid] < data2[j]:
            left = mid + 1
        else:
            right = mid
    data1Minus = data1[left - 1] if left - 1 >= 0 else -9999
    data2[j] = data2[k - 1 - left] if k - 1 - left >= 0 else -9999
    return max(data1Minus, data2[j])


print(solution(dataA, dataB, k))
print(dataA, dataB)
