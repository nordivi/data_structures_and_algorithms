def find_factorial_recursive(number):
    if number == 1:
        return 1

    return number*find_factorial_recursive(number-1)

def find_factorial_iterative(number):
    answer = 1
    for i in range(1, number+1):
        answer *= i
    return answer

a = find_factorial_recursive(5)
print()