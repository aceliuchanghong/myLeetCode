# 股票买卖
# 给出一个数组，第i个元素代表第i天的股票，求最大交易利润。允许最多交易两次。

"""
prices = [1, 3, 1]

[[0, 0], [0, 0], [0, 0]]
[[0, 0], [0, 0], [0, 0]]
[[0, 0], [0, 0], [0, 0]]

Profit = 2
"""
from fromBook.util import generateArray as ga

n = 3
dataB = ga.newArray.generateit(n)


def buyShare(prices):
    """
    三维数组 dp 来记录每一天的最大利润，其中包括交易次数 k 和当前是否持有股票

    第一维表示天数 i，范围是 0 到 n-1，n 是价格数组的长度。
    第二维表示交易次数 k，范围是 0 到 max_k，max_k 是允许的最大交易次数。
    第三维表示当前是否持有股票，0 表示不持有，1 表示持有。
    :param prices:
    :return:
    """
    if not prices:
        return 0
    n = len(prices)
    max_k = 2  # 允许的最大交易次数
    dp = [[[0] * 2 for _ in range(max_k + 1)] for _ in range(n)]
    for _ in dp:
        print(_)

    for i in range(n):
        for k in range(max_k, 0, -1):
            if i == 0:
                dp[i][k][0] = 0  # 第一天不持有股票的利润为0
                dp[i][k][1] = -prices[i]  # 第一天持有股票的利润为负的股价
            else:
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])  # 不持有股票的情况，可以选择保持不动或者卖出
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])  # 持有股票的情况，可以选择保持不动或者买入

    return dp[n - 1][max_k][0]  # 返回最后一天，最大交易次数下不持有股票的利润


print(dataB)
print(buyShare(dataB))
