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

    def remove(self, data):
        if not self.root:
            print("Empty Tree!")

        else:

            curr_node = self.root
            prev_node = curr_node

            while (data):

                if curr_node.dataval == data:

                    # No right child and left child
                    if not curr_node.left and not curr_node.right:

                        if curr_node is prev_node.left:
                            prev_node.left = None
                            del curr_node
                            data = None
                        else:
                            prev_node.right = None
                            del curr_node
                            data = None

                    # No right child
                    elif not curr_node.right:
                        if curr_node is prev_node.left:
                            prev_node.left = curr_node.left
                            del curr_node
                            data = None
                        else:
                            prev_node.right = curr_node.left
                            del curr_node
                            data = None

                    # Right child
                    elif curr_node.right:
                        temp1 = prev_node
                        temp2 = curr_node.left
                        temp3 = curr_node.right
                        temp4 = curr_node

                        prev_node = curr_node
                        curr_node = curr_node.right

                        while (curr_node.left):
                            prev_node = curr_node
                            curr_node = curr_node.left

                        if temp1.left is temp4:
                            temp1.left = curr_node
                        elif temp1.right is temp4:
                            temp1.right = curr_node
                        else:
                            self.root = curr_node

                        curr_node.left = temp2
                        curr_node.right = temp3

                        if curr_node.right is curr_node:
                            curr_node.right = None
                        else:
                            prev_node.left = None

                        del temp4
                        data = None

                elif curr_node.dataval < data:
                    if curr_node.right:
                        prev_node = curr_node
                        curr_node = curr_node.right
                    else:
                        print('Value not in Tree')
                        data = None

                elif curr_node.dataval > data:
                    if curr_node.left:
                        prev_node = curr_node
                        curr_node = curr_node.left
                    else:
                        print('Value not in Tree')
                        data = None





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