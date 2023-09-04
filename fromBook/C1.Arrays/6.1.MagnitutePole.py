# 在一维数组中，找出一个点，使得其所有左边的数字均小于等于它，所有右边的数字都大于等于它。要求在线性时间内返回这个点所在的下标
from fromBook.util import generateArray as ga

k = 2
dataA = ga.newArray.generateit(k)
dataA = [3, 2, 5, 9, 8]


def solution(data):
    if len(data) <= 0:
        return -1
    # 首先,从左到右扫描一遍数组,通过一个辅助布尔数组记录哪些大于等于其之前所有元素的元素
    first, last = data[0], data[len(data) - 1]
    iscurrmax = [False] * len(data)
    for i in range(len(data)):
        if data[i] >= first:
            first = data[i]
            iscurrmax[i] = True
    # 然后,从右到左第二遍扫描数组，如果其后所有元素大于等于当前元素，而且在第一次遍历时当前元素大于等于之前的所有元素，那么程序返回其下标
    for j in range(len(data) - 1, -1, -1):
        if data[j] <= last:
            last = data[j]
            if iscurrmax[j]:
                return j
    return -1


print(dataA)
print(solution(dataA))
