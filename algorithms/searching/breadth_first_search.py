from data_structures.trees.implementation import BinarySearchTree


def breadth_first_search(tree):
    current = tree.root
    nodes_list = []
    queue = [current]
    while len(queue) > 0:
        current = queue.pop(0)
        nodes_list.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return nodes_list

def breath_first_search_recursive(queue, nodes_list):

    if not len(queue):
        return nodes_list
    current = queue.pop(0)
    nodes_list.append(current.value)
    if current.left:
        queue.append(current.left)
    if current.right:
        queue.append(current.right)
    return breath_first_search_recursive(queue, nodes_list)





a = BinarySearchTree()
a.insert(9)
a.insert(4)
a.insert(15)
a.insert(20)
a.insert(1)
a.insert(6)
a.insert(1)
b = breadth_first_search(a)
c = breath_first_search_recursive([a.root], [])
print()

