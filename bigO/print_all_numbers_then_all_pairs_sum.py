

def print_all_numbers_then_all_pair_sums(numbers):
    print('these are the numbers: ')
    for num in numbers: # O(n)
        print(num)

    print('\npair sums: ')
    for n1 in numbers: # O(n)
        for n2 in numbers: # O(n)
            print(n1+n2)
        #O(n*n) = On^2


print_all_numbers_then_all_pair_sums([1,2,3,4,5,6]) # O(n + n^2) = O(n^2)