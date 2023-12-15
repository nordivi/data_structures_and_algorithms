# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
# The left
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
from data_structures.trees.implementation import BinarySearchTree


def validate_binary_search_tree(root):
    queue = [root]
    def recursion(node):


        if node.left:
            if node.left.value >= node.value:
                return False
            queue.append(node.left)
        if node.right:
            if node.right.value <= node.value:
                return False
            queue.append(node.right)
        queue.pop(0)
        return recursion(queue[0]) if queue else True


    return recursion(root)

a = BinarySearchTree()
a.insert(9)
a.insert(4)
a.insert(15)
a.insert(20)
a.insert(1)
a.insert(6)
a.insert(1)
b = validate_binary_search_tree(a.root)
print()
