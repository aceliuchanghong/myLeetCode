# 在一条街上，给H个房子刷墙，要求每个房子刷一种颜色，相邻房子不能刷同一种颜色。每种颜色成本不同，求最小刷墙成本

# dp[i][j]表示刷到第i个房子，并且第i个房子使用第j种颜色的最小刷墙成本。

def min_cost(costs):
    if not costs:
        return 0

    num_houses = len(costs)
    num_colors = len(costs[0])

    # 创建一个二维数组来保存中间结果
    dp = [[0] * num_colors for _ in range(num_houses)]

    # 初始化第一行
    dp[0] = costs[0]

    # 从第二行开始计算最小刷墙成本
    for house in range(1, num_houses):
        for color in range(num_colors):
            # 当前房子刷为color颜色的最小成本
            min_cost = float('inf')
            for prev_color in range(num_colors):
                if prev_color != color:
                    min_cost = min(min_cost, dp[house - 1][prev_color])
            dp[house][color] = min_cost + costs[house][color]

    # 返回最后一行的最小成本
    return min(dp[-1])


def min_cost2(costs):
    if not costs:
        return 0

    num_houses = len(costs)
    num_colors = len(costs[0])

    # 创建一个二维数组来保存中间结果
    dp = [[0] * num_colors for _ in range(num_houses)]

    # 初始化第一行
    dp[0] = costs[0]

    # 从第二行开始计算最小刷墙成本
    for i in range(1, num_houses):
        for j in range(num_colors):
            # 计算刷当前房子为第j种颜色的最小成本
            dp[i][j] = min(dp[i - 1][k] + costs[i][j] for k in range(num_colors) if k != j)

    # 返回最后一行的最小成本
    return min(dp[-1])


# 示例输入 costs是一个二维数组，表示每个房子刷不同颜色的成本
costs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 调用函数并输出结果
print(min_cost(costs))
print(min_cost2(costs))
