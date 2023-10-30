# 给出一个有向图，从A节点走到B节点，正好走N步，有多少种走法？走过的节点可以重复走。
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbor = []