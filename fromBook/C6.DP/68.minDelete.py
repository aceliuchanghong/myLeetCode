# 最长递增子序列
# 给出一个数组，找出最少元素，使得将其删除之后，剩下的元素是递增有序的
# 动态规划
from fromBook.util import generateArray as ga

k = 15
dataA = ga.newArray.generateit(k)


# 删除最少的元素，保证剩下的元素是递增有序的。换一句话说，找出最长的递增有序序列
def find_min_removal(arr):
    n = len(arr)
    # dp[i]代表以输入数组arr[i]为结尾的最长子序列长度，dp[i]通过如下方式计算

    # dp[i] = 1 初始化的时候每个元素自己就是一个最长子序列,就是1
    # dp[i] = max(dp[j] + 1) for j in range(i) if arr[i] > arr[j]

    dp = [1] * n  # 用于保存以每个元素结尾的最长递增子序列的长度

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)  # 这个1其实是加的i这个新元素

    max_length = max(dp)  # 最长递增子序列的长度
    min_removal = n - max_length  # 最少需要删除的元素个数

    return min_removal


arr = [4, 2, 3, 6, 10, 1, 12]
result = find_min_removal(arr)
print(result)
print(dataA)
