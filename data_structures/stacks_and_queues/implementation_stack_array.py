# Podemos usar Arrays ou Linked Lists
# Qual é melhor para cada classe?
# R: Depende para Stack e Linked Lists para Queues


class Stack():
    def __init__(self):
        self.array = []

    def peek(self):
        return self.array[len(self.array) - 1] if self.array else None


    def push(self, value):
        self.array.append(value)
        return self
    def pop(self):
        return self.array.pop()
a = Stack()
a.push(31)
a.push(3)
a.push(4)
a.pop()
b = a.peek()
print()









