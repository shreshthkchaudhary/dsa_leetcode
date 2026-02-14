# 1929. Concatenation of Array

def getConcatenation (nums):
    n=len(nums)
    for i in range (0,n):
        nums.append(nums[i])
    return nums

print(getConcatenation([]))