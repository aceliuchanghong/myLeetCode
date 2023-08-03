# 给定一个整型数组，是否能找出其中的两个数使其和为某个指定的值？输入数组是无序的
data = [1, 5, 7, 3]
target = 10


def hasSum(des=data, src=target):
    if len(des) < 2:
        return False
    des.sort()
    left = 0
    right = len(des) - 1
    while left < right:
        if des[left] + des[right] == src:
            return True
        elif des[left] + des[right] < src:
            left += 1
        else:
            right -= 1
    return False


print(hasSum())
