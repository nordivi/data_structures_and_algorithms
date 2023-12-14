
def bubble_sort(arr):
    sort_count = 0
    while sort_count != len(arr) - 1:
        i = 0
        while i < len(arr) - 1:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            i+=1
        sort_count+=1
    return arr

a = bubble_sort([2,3,4,56,7,3,4,31,3,3])
print()