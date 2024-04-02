import numpy as np


class newArray:
    @classmethod
    def generateit(self, key=6):
        """
        生成一个随机2倍长的数组
        :param key:
        :return:
        """
        deep = key * 2
        return [np.random.randint(0, deep) for _ in range(key)]

    def generateNegOne(self, key: int = 6):
        """
        生成一个随机2倍长的数组
        :param key:
        :return:
        """
        deep = key * 2
        return [np.random.randint(-1 * deep, deep) for _ in range(key)]

    @classmethod
    def generateDiffOne(self, key=10):
        """
        返回2倍无重复值数组
        :param key:
        :return:
        """
        deep = key * 2
        # 返回无重复值数组
        return list(set([np.random.randint(1, deep) for _ in range(key)]))
