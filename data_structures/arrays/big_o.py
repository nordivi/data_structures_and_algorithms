strings = ['a', 'b', 'c', 'd']
# 4x4 = 16 bytes of storage in 32 bits system

strings[2] # O(1)

# push
strings.append('e') # O(1)

# pop
strings.pop() # O(1)

# insert in beggining
strings.insert(0, 'x') # O(n)

# insert in middle
strings.insert(3, 'y') # O(n)


print(strings)
