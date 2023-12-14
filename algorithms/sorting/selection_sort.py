
def selection_sort(arr):

    for i in range(len(arr)):
        min_num = arr[i]
        min_index = i
        for j in range(i+1, len(arr)):
            if min_num > arr[j]:
                min_num = min(min_num, arr[j])
                min_index = j
        arr[min_index], arr[i] = arr[i], min_num

    return arr


a = selection_sort([2,3,4,56,7,3,4,31,3,3])
print()