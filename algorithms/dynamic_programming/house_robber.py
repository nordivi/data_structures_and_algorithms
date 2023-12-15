# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
#
#

def rob(nums) -> int:
    if len(nums) == 1:
        return nums[0]

    if len(nums) == 2:
        return nums[0] if nums[0] > nums[1] else nums[1]

    def dp(i, nums, cache):
        # base case
        if i >= len(nums) - 2 and i < len(nums):
            return nums[i]
        if i >= len(nums) - 1:
            return 0
        # cache
        if i in cache:
            return cache[i]

        rob_next_2 = dp(i + 2, nums, cache)
        rob_next_3 = dp(i + 3, nums, cache)

        max_n = max(rob_next_2, rob_next_3)
        cache[i] = max_n + nums[i]

        return max_n + nums[i]

    cache = {}

    return max(dp(0, nums, cache), dp(1, nums, cache))

a = rob([2,7,9,3,1,4,56,6,3,4,1,23,4,3,5,0])
print()
