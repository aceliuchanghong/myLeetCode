# 设计一个类，包含如下两个成员函数。
# Save（int input）
# 插入一个整数到一个整数集合里。
#（int target）
# 检验是否存在两个数和为输入值。如果存在这两个数，则返回true；否则返回false。
class Solution:
    def __init__(self, data=[]):
        self.data = data

    def save(self, ans):
        self.data.append(ans)

    def test(self, target):
        for i in self.data:
            if target - i in self.data:
                if target - i == i and self.data.count(i) == 1:
                    continue
                return True
        return False


t = Solution([1, 5, 6, 8, 7, 10])
t.save(9)
print(t.test(11))
print(t.test(19))
print(t.test(20))
t.save(10)
print(t.test(20))
