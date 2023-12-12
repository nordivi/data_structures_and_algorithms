# Return first recurring carecter

def first_recurring_char(array):
    count_map = {}
    for i, char in enumerate(array):
        if char in count_map:
            return char
        else:
            count_map[char] = i

    return False

a = first_recurring_char([1,3432,3,4,5,65,76,7,12,2,3432,1,1,2,3,32,5,1,2,45,6,7,3,4,3,2,1,2,3,5,5,7,3,34,1,2,3])
print()