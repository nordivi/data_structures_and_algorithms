class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return self

        currNode = self.root
        while True:
            if value > currNode.value:
                if currNode.right:
                    currNode = currNode.right

                else:
                    currNode.right = new_node
                    return self
            elif value < currNode.value:
                if currNode.left:
                    currNode = currNode.left

                else:
                    currNode.left = new_node
                    return self
            else:
                return None

        return self.root


    def lookup(self, value):
        if not self.root:
            return None
        current_node = self.root
        while current_node:
            if value > current_node.value:
                current_node = current_node.right

            elif value < current_node.value:
                    current_node = current_node.left
            else:
                return current_node
        return None


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
a=tree.lookup(1)
b=tree.lookup(9)
c=tree.lookup(10)

print()