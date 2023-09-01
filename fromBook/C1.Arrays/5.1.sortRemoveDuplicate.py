# 给出一个有序数组，就地移除重复元素，保持每个元素只出现一次并返回新的数组长度
from fromBook.util import generateArray as ga

k = 5
dataA = ga.newArray.generateit(k)
dataA.sort()


# 使用两个下标i和j，其中i记录新数组最后一个元素的位置，j遍历整个数组，通过j移动来移动i。
# 当j和i指向不同值的元素时，把j指向的值拷贝至i指向的元素，然后将i往后移动一位。当j和i指向元素值相同时，不对i做操作，只移动j，以保证i遍历过的元素值各不相同

# 此解法走到最后那个元素的时候有问题
def solution2(data):
    if len(data) <= 0:
        return data
    i, j = 0, 0
    while j < len(data) - 1:
        if i == j:
            j += 1
        elif data[i] != data[j]:
            data[i] = data[j]
            i += 1
        else:
            j += 1
    return i + 1


# 修改
def solution(data):
    if len(data) <= 0:
        return data
    i, j = 0, 0
    # 首先,这儿是0到len(data)并非len(data)-1
    for j in range(0, len(data)):
        if data[j] != data[i]:
            # 此处注意,需要在i+1位置保存data[j]的值,因为下一轮比较的是data[i]的下一个数了
            i += 1
            data[i] = data[j]
    return i + 1


# 如果允许重复元素最多出现两次
def solution3(data):
    if len(data) <= 2:
        return data
    i, j = 0, 0
    for j in range(2, len(data)):
        # 复制俩指针的值不等，或者第二个指针值不等于第一个指针的前一个值
        if data[j] != data[i] or data[j] != data[i - 1]:
            i += 1
            data[i] = data[j]
    return i + 1


print(dataA)
print(solution(dataA))
