# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 示例 2：
# 输入：height = [4,2,0,3,2,5]
# 输出：9
# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105


def trap(height):
    if not height:
        return 0

    n = len(height)
    # 定义了两个数组 left_max 和 right_max 用于记录每个位置左侧和右侧的最大高度
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = height[0]

    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - height[i]

    return water


# 示例输入
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))  # 输出应为 6
