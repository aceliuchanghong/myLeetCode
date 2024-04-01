# 给定一个数组比如[1,1,2,3,5] 一个target值7,输出所有的加起来等于target的子数组,使用dfs解决
# 有一点点类似凑零钱
"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。输入: coins = [1, 2, 5], amount = 11，输出: 3
解释: 11 = 5 + 5 + 1 输入: coins = [2], amount = 3，输出: -1
"""
from fromBook.util import generateArray as ga


def dfs(nums, target, index, path, result):
    if target == 0:
        result.append(path)
        return
    if target < 0 or index == len(nums):
        return
    # 包含当前元素
    dfs(nums, target - nums[index], index + 1, path + [nums[index]], result)
    # 不包含当前元素
    dfs(nums, target, index + 1, path, result)


def find_subarrays(nums, target):
    result = []
    dfs(nums, target, 0, [], result)
    return result


k = 15
dataA = ga.newArray.generateit(k)

nums = [1, 1, 2, 3, 5]
target = 7
print(find_subarrays(nums, target))
print(find_subarrays(dataA, 33))
