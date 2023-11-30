# 设计一数据结构，使插入、删除、搜索、随机访问都是常数时间
class MagicList:
    def __init__(self):
        self.data = []  # 动态数组，存储元素 数据值val集合
        self.index_map = {}  # 散列表，用于元素索引映射

    # [42, 'Hello']
    # {42: 0, 'Hello': 1}
    def insert(self, element):
        if element not in self.index_map:
            index = len(self.data)  # 获取当前元素在数组中的索引
            self.index_map[element] = index  # 将索引存储到散列表中
            self.data.append(element)  # 将元素添加到数组末尾

    def delete(self, element):
        if element in self.index_map:
            index = self.index_map[element]  # 获取索引位置
            del self.index_map[element]  # 从散列表中删除键值对
            last_element = self.data[-1]  # 获取数组末尾元素
            self.data[index] = last_element  # 将末尾元素移到所删除元素的位置
            self.index_map[last_element] = index  # 更新散列表中索引映射
            self.data.pop()  # 删除数组末尾元素

    def search(self, element):
        return element in self.index_map

    def get_random(self):
        import random
        return random.choice(self.data)


# 创建MagicList对象
magic_list = MagicList()

# 插入元素
magic_list.insert(42)
magic_list.insert(7.5)
magic_list.insert("Hello")

# 删除元素
magic_list.delete(7.5)

# 搜索元素
print(magic_list.search(42))  # 输出: True
print(magic_list.search(7.5))  # 输出: False

# 随机访问
print(magic_list.get_random())  # 输出: 42 或者 "Hello"
print(magic_list.data)
print(magic_list.index_map)
