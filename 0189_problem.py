# 189. Rotate Array

def rotate(nums,k):

    n=len(nums)
    if n>k:
        for i in range(k):
            nums.insert(0,nums[n-1])
            nums.pop(n)
    elif n<=k:
        for i in range(k%n):
            nums.insert(0,nums[n-1])
            nums.pop(n)

    return nums
print(rotate([1,2,3,4,5,6,7],71))