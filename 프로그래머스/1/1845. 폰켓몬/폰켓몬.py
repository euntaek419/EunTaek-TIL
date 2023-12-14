def solution(nums):
    nums.sort()
    count = 1
    
    for i in range(0, len(nums)):
        if(nums[i:i+1] != nums[i+1:i+2] and nums[i+1:i+2] != []):
            if(len(nums) // 2 > count):
                count += 1

    return count