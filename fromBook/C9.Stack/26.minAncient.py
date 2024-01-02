# 给定两个节点，求它们在一棵二叉搜索树中的最小公共祖先
# 1.描述一棵二叉搜索树?(二叉搜索树（Binary Search Tree, BST）：是一种特殊的二叉树，对于树中的每个节点，其左子树的所有元素都小于该节点，其右子树的所有元素都大于该节点。)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 2.如何找到结果?
# 可以通过比较给定节点的值来确定它们的最小公共祖先。
# 给定两个节点p和q的值，我们可以使用以下步骤来找到它们的LCA：
# 2.1.从树的根节点开始。
# 2.2.如果p和q的值都小于当前节点的值，则LCA一定在当前节点的左子树中。因此，向左移动到左子节点，然后重复步骤2。
# 2.3.如果p和q的值都大于当前节点的值，则LCA一定在当前节点的右子树中。因此，向右移动到右子节点，然后重复步骤2。
# 2.4.如果p和q的值一个大于当前节点的值，一个小于当前节点的值，或者其中一个就是当前节点的值，则当前节点就是它们的LCA。
def find_min_ancient(tree, node1, node2):
    # 1.判断tree,node1,node2是否存在
    if tree is None:
        return None

    # 如果两个节点值都小于根节点，那么LCA在左子树
    if node1.val < tree.val and node2.val < tree.val:
        return find_min_ancient(tree.left, node1, node2)
    # 如果两个节点值都大于根节点，那么LCA在右子树
    if node1.val > tree.val and node2.val > tree.val:
        return find_min_ancient(tree.right, node1, node2)
    # 如果一个节点值小于等于根节点，另一个节点值大于等于根节点，那么当前根节点就是LCA
    else:
        return tree


# 使用例子
# 构建一棵BST
#       6
#      / \
#     2   8
#    / \ / \
#   0  4 7  9
#     / \
#    3   5

# find_min_ancient(2, 8) = 6
# find_min_ancient(2, 4) = 2
# find_min_ancient(3, 5) = 4

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

p = root.left  # 节点 2
q = root.right  # 节点 8
lca = find_min_ancient(root, p, q)
print(f"LCA of {p.val} and {q.val} is {lca.val}")  # 应该输出 6
print(find_min_ancient(root, root.left.right.left, root.left.right.right).val)
