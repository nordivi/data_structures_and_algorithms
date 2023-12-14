def reverse_string(string):
    if len(string) == 1:
        return string

    last_item = string[-1]
    sliced_string = string[:len(string)-1]
    return last_item + reverse_string(sliced_string)

a = reverse_string('Victor!')
print()