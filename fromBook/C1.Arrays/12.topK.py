# 求一维数组中最小的k个数
# 遗漏点 内存是否能容纳整个数组?
from fromBook.util import generateArray as ga
from fromBook.util.ChangeTwo import exchange

data = ga.newArray.generateit(35)
target = 10


def solution(des=[4, 5, 1, 6, 2, 7, 3, 8], k=4):
    if len(des) < k:
        return des
    des.sort()
    return des[:k]



def solution2(des, k):
    start = 0
    end = len(des) - 1
    # 如果返回的下标是k-1 则OK
    index = partition2(des, start, end)
    print("=:", des)
    while k - 1 != index:
        # des在不停的变化,所以如果 index > k - 1，说明基准元素在第 k 小元素的右边，那么下次划分就对左半部分进行划分
        if index > k - 1:
            end = index - 1
            index = partition2(des, start, end)
            print(">:", des)
        else:
            start = index + 1
            index = partition2(des, start, end)
            print("<:", des)
    return des[:k]


# 快排的分区函数:选择一个数,把比选择的数小的或相等放左边,大的放右边,返回最后分区后选择的数的下标
# 此处基准元素是每个的第一个,所以返回值都一样
def partition2(data, start, end):
    if start > end:
        return -1
    # 随便选一个data里面有的数
    pivot = start

    # 此处把选定的基准元素 pivot 放到数组的最后
    # 在代码的后续处理中，遍历数组将所有小于等于基准元素的值都放到左侧，大于基准元素的值放到右侧
    # 由于基准元素被放置在数组末尾，因此在遍历过程中不会出现与其交换的情况
    data[pivot], data[end] = exchange(data[pivot], data[end])

    # 如果当前遍历的元素 data[i] 小于等于基准元素 data[end],那么说明这个元素应该被放置到基准元素的左边，所以我们将其与 data[pivot] 进行交换
    for i in range(start, end):
        if data[i] <= data[end]:
            if i != pivot:
                # 为什么是与 data[pivot] 进行交换呢？这个 pivot 事实上记录了一个位置：即当前已经找到的所有小于等于基准元素的元素的个数
                # 也可以理解为小于等于基准元素的数组边界。一旦发现一个新的元素小于等于基准元素，就通过交换，将这个元素放到这个边界的左侧
                data[i], data[pivot] = exchange(data[i], data[pivot])
            # 因为某个元素应该被放置到基准元素的左边,所以枢轴pivot+1
            pivot += 1

    # 把基准元素放置到它在排序数组中应该处于的位置,还原数组 为了接下来接着调用不出问题
    data[pivot], data[end] = exchange(data[pivot], data[end])
    return pivot


print(data)
print(solution2(data, target))
