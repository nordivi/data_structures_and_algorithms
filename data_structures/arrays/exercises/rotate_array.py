
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

def rotate(nums, k):
    L = len(nums)
    if L == k: return

    k = k % L  # the case when k > L
    nums.reverse()

    for i in range(k // 2):
        nums[i], nums[k - 1 - i] = nums[k - 1 - i], nums[i]

    for i in range(k, (L + k) // 2):
        nums[i], nums[L - 1 - i + k] = nums[L - 1 - i + k], nums[i]

    return nums

rotate(nums = [1,2,3,4,5,6,7], k = 3)