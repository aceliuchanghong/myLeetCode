# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.
"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

这个并非是典型的dp了,因为每个子问题的最优解,并不一定是全局最优
"""

from fromBook.util import generateArray as ga

k = 6
dataA = ga.newArray.generateit(k)
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


def trap(height):
    if not height:
        return 0
    n = len(height)
    max_left = [0] * n
    max_right = [0] * n

    max_left[0] = height[0]
    max_right[n - 1] = height[n - 1]

    for i in range(1, n):
        max_left[i] = max(height[i], max_left[i - 1])
    for j in range(n - 2, -1, -1):
        max_right[j] = max(height[j], max_right[j + 1])

    water = 0

    for i in range(n):
        water += min(max_left[i], max_right[i]) - height[i]
    return water


print(dataA)
print(trap(dataA))
print(trap(height))
