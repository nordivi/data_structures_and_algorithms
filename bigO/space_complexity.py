

def boooo(n):
    for i in n:
        print('booo!')


boooo([1,2,3,4,5]) # space complexity of O(1) -- i is not being used. its still O(n) time complexity


def hi_n_times(n):
    hi_array = {}
    for i in range(n):
        hi_array[i] = 'hi' # its using the index
    print(hi_array)
    return hi_array

hi_n_times(5) # O(n) - each item is a new memory space