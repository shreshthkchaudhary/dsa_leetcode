# 1. Two Sum

def twoSum (nums,target):
    n=len(nums)
    print(n)
    for i in range (n):
        for j in range (i+1,n):
            if nums[i]+nums[j]==target:
                return[i,j]
print(twoSum([1,2,3,4,5,6],11))




# def twoSum (nums,target):
#     arr=[]
#     for i in range(len(nums)-1):
#         for j in range(1,len(nums)):
#             if nums[i]!=nums[j]:
#                 if nums[i]+nums[j]==target:
#                     arr.append(i)
#                     arr.append(j)
#                     break
#     return arr
# print(twoSum([2,3,4],6))