import numpy as np


class newArray:
    def generateit(self=10):
        deep = self * 2
        return [np.random.randint(0, deep) for i in range(self)]

    def generateDiffOne(self=10):
        deep = self * 2
        # 返回无重复值数组
        return list(set([np.random.randint(0, deep) for i in range(self)]))
