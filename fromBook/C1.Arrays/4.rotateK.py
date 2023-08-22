# 返回将一维数组向右旋转k个位置的结果。比如，一维数组[1,2,3,4,5]，k=2时，返回结果是[4,5,1,2,3]。要求常数级空间复杂度，允许修改原有数组

from fromBook.util import generateArray as ga
from fromBook.util.ChangeTwo import exchange

dataset = ga.newArray.generateit(5)
k = 2


# 采用分而治之
def solution(data, target):
    if len(data) <= target or len(data) == 0:
        return data
    reverse(data, 0, len(data) - 1)
    reverse(data, 0, target - 1)
    reverse(data, target, len(data) - 1)
    return data


def reverse(data, start, end):
    while start < end:
        data[start], data[end] = exchange(data[start], data[end])
        end = end - 1
        start = start + 1


print(dataset)
print(solution(dataset, k))
