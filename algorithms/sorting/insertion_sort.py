
def insertion_sort(arr: list):
    # go over the list, start with the second index
    for i in range(1, len(arr)):
        # store the second item in "j" variable
        j = i
        # ask if the first item in the list is greater than the second item in the list
        # if true, swap them and go further "left" in the list by decrementing "j"
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr


a = insertion_sort([2,3,4,56,7,3,4,31,3,3])
