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
