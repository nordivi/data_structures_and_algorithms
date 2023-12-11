class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def access(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        last_item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -=1
        return last_item

    def delete(self, index):
        item = self.data[index]
        self.shiftItems(index)
        del self.data[self.length-1]
        self.length -=1
        return item
    def shiftItems(self, index):
        while index < self.length -1:
            self.data[index] = self.data[index+1]
            index+=1

array = MyArray()
array.push(3)
array.access(0)
array.push('!')
array.delete(1)
array.length
print()