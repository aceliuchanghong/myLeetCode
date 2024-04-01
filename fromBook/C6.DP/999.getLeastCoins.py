"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。输入: coins = [1, 2, 5], amount = 11，输出: 3
解释: 11 = 5 + 5 + 1 输入: coins = [2], amount = 3，输出: -1
"""

coins = [1, 2, 5]
target = 33


def my_dp(target, coins=None):
    """
    设dp[target]为达到target的最小硬币数
    那么 dp[target] = dp[target - coins[i]] + 1
    而dp[1]=1
    :param coins:
    :param target:
    :return:
    """
    if coins is None:
        coins = [1, 2, 5]
    for i in range(len(coins)):
        pass


# 另外的  f(n) = min{ f(n-1)，f(n-2)，f(n-5) } + 1
def coin_change(coins, amount):
    # 创建一个长度为amount+1的列表，初始值为无穷大（表示无法凑成）
    dp = [float('inf')] * (amount + 1)
    # 金额为0时，所需硬币数量为0
    dp[0] = 0

    # 逐个计算从1到amount的所需硬币数量,左闭右开
    for i in range(1, target + 1):
        for coin in coins:
            # 如果当前面额小于等于当前金额，则尝试使用该硬币
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount]


print(coin_change(coins, target))


# 以上只是求出了凑成零钱的的最小数量，但如果想求由哪些面值的硬币构成的，该如何修改呢？
def coin_change2(coins, amount):
    # 创建一个长度为amount+1的列表，用于记录最少硬币数量
    dp = [float('inf')] * (amount + 1)
    # 创建一个长度为amount+1的列表，用于记录最后一枚硬币的面额
    last_coin = [-1] * (amount + 1)
    # 目标金额为0时，所需硬币数量为0
    dp[0] = 0

    # 逐个计算从1到amount的所需硬币数量
    for i in range(1, amount + 1):
        # 遍历硬币面额
        for coin in coins:
            # 如果当前面额小于等于当前金额，则尝试使用该硬币
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                # 更新所需硬币数量和最后一枚硬币的面额
                dp[i] = dp[i - coin] + 1
                last_coin[i] = coin

    # 如果dp[amount]仍为初始值，则说明无法凑成该金额，返回-1
    if dp[amount] == float('inf'):
        return -1

    # 回溯找出构成目标金额的硬币面额
    coins_used = []
    while amount > 0:
        coins_used.append(last_coin[amount])
        amount -= last_coin[amount]

    return coins_used


print(coin_change2(coins, target))
