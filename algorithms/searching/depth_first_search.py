from data_structures.trees.implementation import BinarySearchTree

def depth_first_search_in_order(tree):
    node = tree.root
    return traverse_in_order(node, [])

def traverse_in_order(node, nodes_list):
    if node.left:
        traverse_in_order(node.left, nodes_list)
    nodes_list.append(node.value)
    if node.right:
        traverse_in_order(node.right, nodes_list)

    return nodes_list
def depth_first_search_post_order(tree):
    node = tree.root
    return traverse_post_order(node, [])

def traverse_post_order(node, nodes_list):

    if node.left:
        traverse_post_order(node.left, nodes_list)

    if node.right:
        traverse_post_order(node.right, nodes_list)
    nodes_list.append(node.value)
    return nodes_list

def depth_first_search_pre_order(tree):
    node = tree.root
    return traverse_pre_order(node, [])

def traverse_pre_order(node, nodes_list):
    nodes_list.append(node.value)
    if node.left:
        traverse_pre_order(node.left, nodes_list)

    if node.right:
        traverse_pre_order(node.right, nodes_list)

    return nodes_list


a = BinarySearchTree()
a.insert(9)
a.insert(4)
a.insert(15)
a.insert(20)
a.insert(1)
a.insert(6)
a.insert(1)
b = depth_first_search_in_order(a)
c = depth_first_search_pre_order(a)
d = depth_first_search_post_order(a)
print()