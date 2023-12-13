# Return first recurring carecter

def first_recurring_char(array):
    count_map = {}
    for i, char in enumerate(array):
        if char in count_map:
            return char
        else:
            count_map[char] = i

    return False
