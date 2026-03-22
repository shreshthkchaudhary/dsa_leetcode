# 704. Binary Search

def search(nums, target):
    l,h=0,len(nums)-1
    while l<=h:
        m=(l+h)//2
        if nums[m]==target:
            return m
        elif nums[m]<target:
            l=m+1
        else:
            h=m-1

    return -1

print(search([-1,0,3,5,9,12],9))