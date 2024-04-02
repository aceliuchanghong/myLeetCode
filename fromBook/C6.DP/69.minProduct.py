# 最小化数组乘积
# 给出两个数组A和B，两个数组大小分别为m和n，其中m<n。现要求将（n-m）个0插入A(0可以随便插入,且不一定在一起)，使得A*B的值最小，求其最小乘积
from fromBook.util import generateArray as ga

m, n = 10, 15
dataA = ga.newArray.generateNegOne(m)
dataB = ga.newArray.generateit(n)


# dp[i][j] 表示将 A 的前 i 个元素和 B 的前 j 个元素进行乘积运算得到的最小乘积。
#
# 对于 dp[i][j]，考虑以下两种情况：
# 1. 若 A[i-1] 与 B[j-1] 不插入 0，则 dp[i][j] = dp[i-1][j-1] + A[i-1] * B[j-1]。
# 2. 若在 A[i-1] 处插入 0，则 dp[i][j] = dp[i-1][j] + 0 * B[j-1]。
#
# 状态转移方程为：
# dp[i][j] = min(dp[i-1][j-1] + A[i-1] * B[j-1], dp[i-1][j] + 0 * B[j-1])
#
# 初始条件为：
# dp[0][0] = A[0] * B[0]

def solution(A, B):
    m = len(A)
    n = len(B)
    # 其实是大小为（m+1）x（n+1）的二维数组dp
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = A[0] * B[0]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i - 1][j - 1] + A[i - 1] * B[j - 1], dp[i][j - 1], dp[i - 1][j])

    return dp[m][n]


print(dataA)
print(dataB)
print(solution(dataA, dataB))
A = [1, 2, 3]
B = [4, 5, 6, 7, 8]
print(solution(A, B))
