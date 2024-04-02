"""
题目描述：给定一个不重复的数组和一个目标数，找出数组中所有可以组合成目标数的组合。
经典题目：组合总和（Combination Sum），LeetCode上的39题。
示例：给定数组 [2, 3, 6, 7] 和目标数 7，找出所有可以组合成目标数 7 的组合：[2, 2, 3] 和 [7]。
"""
from fromBook.util import generateArray as ga

k = 8
candidates = ga.newArray.generateDiffOne(k)
target = 20
print(candidates)


def combination_sum(candidates, target):
    if not candidates or target < 0:
        return []

    # start: 用于避免重复搜索已经搜索过的数字，表示当前递归搜索的起始位置。
    def dfs(start, target, path):
        if target == 0:  # 如果目标数为0，说明找到了一个符合条件的组合，将其添加到结果列表中
            result.append(path)
            return
        if target < 0:  # 如果目标数小于0，说明当前组合不符合条件，直接返回
            return
        for i in range(start, len(candidates)):  # 从start位置开始遍历数组
            dfs(i, target - candidates[i], path + [candidates[i]])  # 递归调用dfs，继续搜索下一个组合

    result = []
    dfs(0, target, [])
    return result


print(combination_sum(candidates, target))
