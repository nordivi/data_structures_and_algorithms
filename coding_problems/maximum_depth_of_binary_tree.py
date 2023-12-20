# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
from data_structures.trees.implementation import BinarySearchTree


def max_depth(root):
    def dfs(root, depth):
        if not root: return depth
        return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

    return dfs(root, 0)

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
a = max_depth(tree.root)
print()

