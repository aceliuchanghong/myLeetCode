# 输入两个单词word1和word2，求出从word1转换为word2的最少步骤。每个转换操作算一步。转换操作限定于：删除一个字符，插入一个字符和替换一个字符
# dp[i][j]表示将word1的前i个字符转换为word2的前j个字符的最小步骤数。即从word1[0…i-1]转换为word2[0…j-1]的最少步骤

# 当word1[i-1] 和 word2[j-1] 字符相等时候，dp[i][j] = dp[i-1][j-1]
# 否则dp[i][j] = 1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) 插入word1,插入word2,替换

def min_distance(word1, word2):
    len1, len2 = len(word1), len(word2)

    # 初始化数组
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # 初始化第一行和第一列
    for i in range(len1 + 1):
        dp[i][0] = i
    for j in range(len2 + 1):
        dp[0][j] = j

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[len1][len2]


# 示例输入
word1 = "horse"
word2 = "ros"

# 调用函数并输出结果
print(min_distance(word1, word2))
