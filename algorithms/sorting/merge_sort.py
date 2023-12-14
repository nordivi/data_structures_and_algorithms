
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    left = arr[:int(len(arr) / 2)]
    right = arr[int(len(arr) / 2):]
    print('Left: ', left)
    print('Right: ', right)
    return merge(
        merge_sort(left),
        merge_sort(right)
    )

def merge(left,right):
    i = 0
    j = 0
    newlist = []
    while i < len(left) and j < len(right):
        if (left[i] <= right[j]):
            newlist.append(left[i])
            i += 1
        else:
            newlist.append(right[j])
            j += 1
    while i < len(left):
        newlist.append(left[i])
        i += 1
    while j < len(right):
        newlist.append(right[j])
        j += 1
    return newlist

a = merge_sort([2,3,4,56,7,3,4,31,3,3])
print()
