# 给出一个无序的整型数组，找出最长连续元素序列的长度。时间复杂度要求在线性时间内。
def longest_consecutive(nums):
    num_set = set(nums)  # 将数组转换为集合来去除重复元素，并且提供O(1)的查找时间
    longest_streak = 0

    for num in num_set:
        # 只有当当前数字不是某个序列的中间部分时，才开始计算序列长度
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # 查找当前数字后面的连续数字
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # 更新最长序列的长度
            longest_streak = max(longest_streak, current_streak)

    return longest_streak


nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))  # 输出应该是4，因为最长连续序列是[1, 2, 3, 4]
