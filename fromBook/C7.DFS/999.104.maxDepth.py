# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest
# leaf node.
"""
fromBook/util/files/dfs/img.png

Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2

root = [3, 9, 20, NULL, NULL, 15, 7]
"""
from fromBook.util.TreeNode import TreeNode

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


def maxDepth(root: TreeNode):
    if root is None:
        return 0
    else:
        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)
    return max(left_depth, right_depth) + 1


print(maxDepth(root))
