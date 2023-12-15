# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climb_stairs(n):
    cache = {}
    def caching(i):
        if i in cache:
            return cache[i]
        if i < 4:
            cache[i] = i
            return cache[i]
        cache[i] = caching(i-1) + caching(i-2)
        return cache[i]



    return caching(n)

a = climb_stairs(6)
print()