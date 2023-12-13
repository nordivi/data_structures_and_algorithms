# Podemos usar Arrays ou Linked Lists
# Qual é melhor para cada classe?
# R: Depende para Stack e Linked Lists para Queues

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top


    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        if self.length == 0:
            self.bottom = new_node
        self.length+=1
        return self
    def pop(self):
        poped_item = self.top
        self.top = self.top.next
        self.length-=1
        return poped_item
a = Stack()
a.push(31)
a.push(3)
a.push(4)
a.pop()
b = a.peek()
print()









