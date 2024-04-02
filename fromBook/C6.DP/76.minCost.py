# 在一条街上，给H个房子刷墙，要求每个房子刷一种颜色，相邻房子不能刷同一种颜色。每种颜色成本不同，求最小刷墙成本

# Q:为什么不直接找出价格最低的2个,轮换着使用就最低了
# A:因为是做动态规划,换个思想做

# dp[i][j]表示刷到第i个房子，并且第i个房子使用第j种颜色的最小刷墙成本。


def min_cost(costs):
    if not costs:
        return 0

    num_houses = len(costs)
    num_colors = len(costs[0])

    # 创建一个二维数组来保存中间结果
    dp = [[0] * num_colors for _ in range(num_houses)]
    print(dp)

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
