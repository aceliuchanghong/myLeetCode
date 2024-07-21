import threading


class SingletonPattern:
    __instance = None

    def __new__(cls, *args, **kwargs):
        """
        __new__ 是一个静态方法不需要显式地使用 @staticmethod 装饰器，它在对象实例化时首先被调用。
        cls 是类本身的一个引用，类似于实例方法中的 self 参数，但 cls 代表的是类而不是实例。
        :param args:
        :param kwargs:
        """
        if not cls.__instance:
            cls.__instance = super(SingletonPattern, cls).__new__(cls, *args, **kwargs)
        return cls.__instance


class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        """
        further:
        使用锁机制实现线程安全单例模式
        :param args:
        :param kwargs:
        """
        with cls._lock:
            if not cls._instance:
                cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    s1 = SingletonPattern()
    s2 = SingletonPattern()
    print(s1 is s2)
