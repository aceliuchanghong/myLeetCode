import numpy as np


class newArray:
    def generateit(self=10):
        deep = self * 2
        return [np.random.randint(0, deep) for i in range(self)]

    def generateDiffOne(self=10):
        deep = self * 2
        # 返回如果没有该数则添加到数组中
        return list(set([np.random.randint(0, deep) for i in range(self)]))
