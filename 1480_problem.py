# 1480. Running Sum of 1d Array

def runningSum (nums):
    # n=len(nums)
    # if n>1:
    #     s=1
    #     count=nums[0]
    #     new=[]
    #     new.append(nums[0])
    #     for i in nums[s:n]:
    #         a=i+count
    #         count=a
    #         new.append(a)
    
    #     return new
    # else:
    #     return [nums[0]]

    n=len(nums)
    for i in range(1,n):
        nums[i]=nums[i]+nums[i-1]
    return nums



print(runningSum([1,2,3,4]))