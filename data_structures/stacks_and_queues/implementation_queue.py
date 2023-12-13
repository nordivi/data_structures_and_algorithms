# Podemos usar Arrays ou Linked Lists
# Qual é melhor para cada classe?
# R: Depende para Stack e Linked Lists para Queues

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first


    def enqueue(self, value):
        new_node = Node(value)
        if not self.length:
            self.first, self.last = new_node, new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length+=1
        return self
    def dequeue(self):
        if not self.first:
            return None
        if self.first == self.last:
            self.last = None
        poped_item = self.first
        self.first = self.first.next
        self.length -= 1
        return poped_item
a = Stack()
a.enqueue(31)
a.enqueue(3)
a.enqueue(4)
a.dequeue()
b = a.peek()
print()









