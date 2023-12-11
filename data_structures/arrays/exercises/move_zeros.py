def move_zeros(nums):
    loop_index = 0
    i=0
    while loop_index < len(nums) - 1:
        if not nums[i]:
            del nums[i]
            nums.append(0)
        else:
            i+=1
        loop_index += 1
    return nums

move_zeros([0,1,0,3,12])