

def cache_fibonacci():
    cache = {}
    def fibonacci(n):
        if n in cache:
            print('Saving time!')
            return cache[n]
        if n < 2:
            return n
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]
    return fibonacci

cache = cache_fibonacci()
cache_fibonacci = cache(2)
cache_fibonacci = cache(3)
cache_fibonacci = cache(5)
cache_fibonacci = cache(7)
cache_fibonacci = cache(4)
cache_fibonacci = cache(2)
print()

