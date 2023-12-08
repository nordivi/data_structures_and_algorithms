# Given 2 arrays, create a function that lets a user know (true or false)
# whether these two arrays contain any common items

from collections import defaultdict
def contains_common_item(array1, array2):
    if len(array1) < len(array2):
        short_array, large_array = array1, array2
    else:
        short_array, large_array = array2, array1
    for element in short_array:
        if element in large_array:
            return True

    return False




contains_common_item(['1', 'x', '4', '2'], ['1', 'fs'])