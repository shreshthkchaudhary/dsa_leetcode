# 75. Sort Colors

def sortColors(nums):
    # nums.sort()
    # return nums
    for i in range(len(nums)-1):
        for j in range (i+1,len(nums)):
            if nums[i]>nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
                # sort(nums)
    return nums

print(sortColors([2,0,2,1,1,0]))