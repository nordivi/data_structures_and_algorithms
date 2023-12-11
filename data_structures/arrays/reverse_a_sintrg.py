def reverse(string):
    if not isinstance(string, str):
        return False
    list_array = list(string)[::-1]
    return ''.join(list_array)

print(reverse('Oi, sou Victor'))