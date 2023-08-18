# 求一维数组中最小的k个数
def solution(des=[4, 5, 1, 6, 2, 7, 3, 8], k=4):
    if len(des) < k:
        return des
    des.sort()
    return des[:k]


# 选中一个数,把比选择的数小的放左边,大的放右边,返回最后分区后选择的数的下标
def partition(data, start, end):
    if start > end:
        return -1
    index = start  # 可以随机选择，不一定是第一个元素

    # 第一次交换
    tmp = data[index]
    data[index] = data[end]
    data[end] = tmp

    for i in range(start, end):
        if data[i] <= data[end]:
            tmp = data[i]
            if i != index:
                # 第二次交换
                tmp = data[index]
                data[index] = data[i]
                data[i] = tmp
            index += 1
    # 第三次交换
    tmp = data[end]
    data[end] = data[index]
    data[index] = tmp
    return index


def solution2(des=[4, 5, 1, 6, 2, 7, 3, 8], k=4):
    start = 0
    end = len(des) - 1
    index = partition(des, start, end)
    while k - 1 != index:
        if index > k - 1:
            end = index - 1
            index = partition(des, start, end)
        else:
            start = index + 1
            index = partition(des, start, end)
    return des[:k]


print(solution())
print(solution2())
