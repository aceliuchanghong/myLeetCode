# 给出两个字符串s1和s2，返回其最大的公共子串
# 1.dp[i][j]记录的是从s1的开始字符到s1的第i个字符组成的字符串，和从s2的开始字符到第j个字符组成的字符串，这两个字符串的最大公共子串长度

def longest_common_substring(s1, s2):
    m, n = len(s1), len(s2)

    # 创建一个二维数组来保存中间结果
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    max_len = 0  # 记录最长公共子串的长度
    end_index = 0  # 记录最长公共子串的结束索引

    # 计算公共子串
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_index = i  # 记录最长公共子串的结束索引

    start_index = end_index - max_len  # 计算最长公共子串的起始索引
    longest_common_substring = s1[start_index:end_index]

    return longest_common_substring


# 示例输入
s1 = "abcdef"
s2 = "xbcde"

# 调用函数并输出结果
print(longest_common_substring(s1, s2))
