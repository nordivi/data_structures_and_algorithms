 #Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def contains_duplicate(nums):
    seen = {}
    for num in nums:
        if num in seen: return True
        else: seen.add(num)
    return False