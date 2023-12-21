# 实现LRU缓存类，至少包含get和put成员函数。get和put算是对元素的一次访问
# LRU（Least Recently Used）缓存是一种常见的缓存淘汰算法，它会淘汰最长时间未被访问的数据。直译为最近最少使用缓存算法
# 当有新的内容需要添加到缓存中时，就需要舍弃一部分原有的内容，LRU的原则就是将最近最少使用的内容替换掉。
# 在Python中，我们可以使用OrderedDict来实现一个简单的LRU缓存，因为OrderedDict可以记住元素被插入的顺序，同时它的popitem方法可以用来弹出最早插入或最近插入的键值对
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            # This line moves the key to the end to show that it was recently used
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value if key exists
            self.cache[key] = value
            # Move the key to the end to show that it was recently used
            self.cache.move_to_end(key)
        else:
            # Add the new key-value pair to the cache
            self.cache[key] = value
            # If the cache is full, remove the first item
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)  # pop the first item


# Example usage
lru_cache = LRUCache(2)
lru_cache.put(1, 1)  # cache is {1=1}
lru_cache.put(2, 2)  # cache is {1=1, 2=2}
print(lru_cache.get(1))  # returns 1
lru_cache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lru_cache.get(2))  # returns -1 (not found)
lru_cache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lru_cache.get(1))  # returns -1 (not found)
print(lru_cache.get(3))  # returns 3
print(lru_cache.get(4))  # returns 4
