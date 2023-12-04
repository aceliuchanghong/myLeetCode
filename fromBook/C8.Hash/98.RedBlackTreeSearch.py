# 对数时间范围查询 设计一个键与值数据结构，至少实现如下两个查找功能：查找单个key，以及支持在给出key范围内查找

# 常见类型的树：
# 二叉树（Binary Tree）：每个节点最多有两个子节点，通常称为左子节点和右子节点。
#
# 二叉搜索树（Binary Search Tree, BST）：是一种特殊的二叉树，对于树中的每个节点，其左子树的所有元素都小于该节点，其右子树的所有元素都大于该节点。
#
# 平衡二叉搜索树（Balanced Binary Search Tree）：是二叉搜索树的一种，它通过自动保持树的高度最小来优化搜索操作。红黑树和AVL树是两种常见的平衡二叉搜索树。
#
    # a. AVL树
    # AVL树是最早被发明的自平衡二叉搜索树。在AVL树中，每个节点的两个子树的高度差被严格控制在1以内。这意味着AVL树是高度平衡的，但可能需要频繁的旋转来维持这种平衡。
    #     树的高度是从该节点到其最远的叶子节点的最长路径上的边的数量。
    #     左子树的高度是指左子节点到其最远的叶子节点的最长路径上的边的数量。
    #     右子树的高度是指右子节点到其最远的叶子节点的最长路径上的边的数量
    #     二叉树的平衡通常指的是树的任何一个节点的两个子树的高度差都不超过1
    # b. 红黑树
    # 红黑树是一种近似平衡的二叉搜索树，它确保任何一个节点的路径到其叶子节点的每个路径都不会长于其他路径的两倍。且需要表示节点R/B颜色。
#
# B树和B+树：这些是自平衡的树数据结构，允许每个节点有多个子女来保持平衡,它们保持数据排序并允许搜索、顺序访问、插入和删除。它们通常用于数据库和文件系统。


# 要设计一个支持对数时间范围查询的数据结构，我们可以使用平衡二叉搜索树（BST），如红黑树或AVL树
from sortedcontainers import SortedDict


class RangeQueryDict:
    def __init__(self):
        self.data = SortedDict()

    def insert(self, key, value):
        self.data[key] = value

    def find(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return None

    def find_range(self, key1, key2):
        # 这将返回一个从key1到key2的键值对的迭代器，包含key1但不包含key2
        return self.data.irange(key1, key2, inclusive=(True, False))


# 示例使用
rqd = RangeQueryDict()
rqd.insert(1, 'a')
rqd.insert(2, 'b')
rqd.insert(3, 'c')

print(rqd.find(2))  # 输出 b

# 打印范围查询结果
for key in rqd.find_range(1, 3):
    print(key, rqd.find(key))
