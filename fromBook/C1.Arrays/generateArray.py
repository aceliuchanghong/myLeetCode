import numpy as np


class newArray:
    def generateit(self, key=10):
        deep = key * 2
        return [np.random.randint(0, deep) for i in range(key)]

    def generateDiffOne(self, key=10):
        deep = key * 2
        # 返回无重复值数组
        return list(set([np.random.randint(0, deep) for i in range(key)]))

# t = newArray().generateit(5)
# print(t)
