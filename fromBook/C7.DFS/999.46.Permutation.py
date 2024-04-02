# Given an array nums of distinct integers, return all the possible permutations.
# You can return the answer in any order.
"""
排列问题（Permutations）：

题目描述：给定一个不重复的数组，求出这个数组的所有排列方式。
经典题目：全排列（Permutations），LeetCode上的46题。
示例：给定数组 [1, 2, 3]，输出所有可能的排列：[1, 2, 3]、[1, 3, 2]、[2, 1, 3]、[2, 3, 1]、[3, 1, 2]、[3, 2, 1]。
"""

dataA = [5, 9, 8, 1, 4, 10]
dataB = [1, 2, 3]


def permutations(array):
    if not array:
        return []

    def dfs(current, remaining):
        if not remaining:
            result.append(current)
            return
        for i in range(len(remaining)):
            dfs(current + [remaining[i]], remaining[:i] + remaining[i + 1:])

    result = []
    dfs([], array)
    return result


for perm in permutations(dataA):
    print(perm)
for perm in permutations(dataB):
    print(perm)
