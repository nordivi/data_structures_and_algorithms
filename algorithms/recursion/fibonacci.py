

def fibonacci_iterative(n): # O(n)
    start = [0, 1]
    while len(start) != n + 1:
        start.append(start[-1] + start[-2])
    return start[-1]


def fibonacci_recursive(n): # O(2^n)
    if n < 2:
        return n
    return fibonacci_iterative(n-1) + fibonacci_iterative(n-2)

a = fibonacci_iterative(4)
b = fibonacci_recursive(8)
print()