
def quick_sort(arr, start, end):
    if start < end:
        p = partition(arr, start, end)
        quick_sort(arr, start, p - 1)
        quick_sort(arr, p + 1, end)

def partition(arr, start, end):
    ptr = start
    pivot = end
    for i in range(start, end):
        if arr[i] <= arr[pivot]:
            arr[ptr], arr[i] = arr[i], arr[ptr]
            ptr += 1
    arr[ptr], arr[pivot] = arr[pivot], arr[ptr]
    return ptr