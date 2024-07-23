"""
组合模式
"""

from abc import ABC, abstractmethod


# 定义文件系统的基本接口
class FileSystemItem(ABC):
    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def remove(self, item):
        pass

    @abstractmethod
    def display(self):
        pass


# 定义目录（组合对象）
class Directory(FileSystemItem):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, item):
        self.children.append(item)

    def remove(self, item):
        self.children.remove(item)

    def display(self, indent=''):
        print(indent + self.name + '/')
        for child in self.children:
            child.display(indent + '    ')


# 定义文件（叶子对象）
class File(FileSystemItem):
    def __init__(self, name):
        self.name = name

    def add(self, item):
        raise Exception('Files cannot have children')

    def remove(self, item):
        raise Exception('Files cannot remove children')

    def display(self, indent=''):
        print(indent + self.name)


if __name__ == '__main__':
    root = Directory('root')
    root.add(Directory('bin'))
    root.add(Directory('usr'))

    root.children[0].add(File('bash'))
    root.children[0].add(File('ls'))

    root.children[1].add(Directory('bin'))
    root.children[1].children[0].add(File('more'))

    root.display()
