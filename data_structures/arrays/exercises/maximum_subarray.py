# Given an integer array nums, find the
# subarray
#  with the largest sum, and return its sum.
def max_subarray(nums):
    r = 0
    res = float('-inf')  # Initialize res to negative infinity for comparison
    prod = 0
    length = len(nums)

    while r < length:
        prod = prod + nums[r]
        res = max(res, prod)

        if prod < 0:
            # If the current sum is negative, reset the window
            prod = 0

        r += 1

    return res

max_subarray([1,2,-1,-5,2,1,-2,1,4,-5,4])