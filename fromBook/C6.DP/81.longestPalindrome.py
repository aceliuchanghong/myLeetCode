# 输入一字符串S，找出其最长回文子串（plindromic substring）
# 例如：输入“abbcbbd”，输出“bbcbb”
def longest_palindrome(word):
    if len(word) <= 1:
        return len(word)

    # 二维布尔数组的元素dp[i][j]记录从s[i]到s[j]组成的子串是否为回文子串
    n = len(word)
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True
    # 记录最长回文子串的起始位置,最长回文子串的长度
    start, max_len = 0, 1

    for i in range(1, n):
        for j in range(i):
            if word[i] == word[j] and (i - j <= 2 or dp[j + 1][i - 1]):
                dp[j][i] = True
                cur_len = i - j + 1
                if cur_len > max_len:
                    max_len = cur_len
                    start = j
    return word[start:start + max_len]


# 示例输入
s = "abbcbbd"

# 调用函数并输出结果
print(longest_palindrome(s))

# self
# 二维布尔数组的元素dp[i][j]记录从s[i]到s[j]组成的子串的回文子串长度
# for i in range(1, n):
#     for j in range(i):
# dp[i][j] = max(2+dp[i-1][j+1],dp[i-1][j],dp[i][j+1])
