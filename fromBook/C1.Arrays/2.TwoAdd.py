# 给定一个整型的数组，找出其中的两个数使其和为某个指定的值，并返回这两个数的下标（数组下标是从0开始）。假设数组元素的值各不相同，则要求时间复杂度为O（n），n为数组的长度
import generateArray as ga

data = ga.newArray.generateDiffOne(5)
target = 10


def solution(dataset=data, targetset=target):
    if len(dataset) < 2:
        return [-1, -1]
    # 循环读取dataset加入哈希表
    hashmap = {}
    for i, num in enumerate(dataset):
        if targetset - num in hashmap:
            return [hashmap[targetset - num], i]
        hashmap[num] = i
    return []


print(data)
print(solution())
