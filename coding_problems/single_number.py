

def single_number(nums):
    seen = {}
    for num in nums:
        if num in seen:
            del seen[num]
        else:
            seen[num] = None
    return list(seen.keys())[0]

b = single_number([4,1,2,1,2])
print()