# 给定一个整型数组，找出最大下标距离j-i，当且仅当A[i]<A[j]和i<j

# 直观的方案是对每个元素，从其后找出比其大的元素，并计算两者下标的差值，取差值中的最大值。该方案时间复杂度为O（n2)
# n为数组长度。那么有没有更快的解决方法？

from fromBook.util.generateArray import newArray

dataset = newArray.generateit(15)


def solution(data):
    if len(data) < 2:
        return -1
    start = 0
    end = len(data) - 1
    while start < end:
        if data[start] < data[end]:
            print(start, end)
            return end - start
        else:
            if data[start] < data[end - 1]:
                end = end - 1
            else:
                start = start + 1


print(dataset)
print(solution(dataset))
