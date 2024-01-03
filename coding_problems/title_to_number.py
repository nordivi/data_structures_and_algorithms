

# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

def title_to_number(column_title):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters_dict = {}
    for i, letter in enumerate(alphabet):
        letters_dict[letter] = i + 1
    res = 0
    L = len(column_title)
    for i in range(L):
        res += (26 ** (L - i - 1)) * (letters_dict[column_title[i]])
    return res

A = title_to_number('A')
print()