# 给出一个有向图，从A节点走到B节点，正好走N步，有多少种走法？走过的节点可以重复走。
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.nexts = []


def count_paths(source, destination, steps):
    # 如果步数为0，且源节点就是目的节点，则找到一条路径
    if steps == 0:
        return 1 if source == destination else 0
    # 如果步数不为0，但是源节点没有相邻的节点，则无法继续走下去
    if not source.nexts:
        return 0
    # 初始化路径数量为0
    path_count = 0
    # 遍历所有相邻的节点
    for neighbor in source.nexts:
        # 对每个相邻节点，递归地寻找剩余步数的路径
        path_count += count_paths(neighbor, destination, steps - 1)
    return path_count


# 有向图的节点java定义如下：
#      class GraphNode{
#         int val;
#         ArrayList<GraphNode> nexts;
#      }

# 使用示例
# 假设我们有以下有向图:
# A -> B, A -> C, B -> D, C -> D, D -> B
# 我们要找从A到D，正好走3步的路径数量
# 创建图节点
A = GraphNode('A')
B = GraphNode('B')
C = GraphNode('C')
D = GraphNode('D')

# 建立连接
A.nexts = [B, C]
B.nexts = [D]
C.nexts = [D]
D.nexts = [B]

print(count_paths(A, D, 2))


# leetcode 第70题类似
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

def climbStairs(n: int):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        # 爬到第 n 级台阶可以由爬到第 n-1 级台阶再爬一步或者爬到第 n-2 级台阶再跨两步得到
        # 所以爬到第 n 级台阶的方法数等于爬到第 n-1 级台阶的方法数加上爬到第 n-2 级台阶的方法数
        s1 = climbStairs(n - 1)
        s2 = climbStairs(n - 2)
        return s1 + s2


print(climbStairs(3))
