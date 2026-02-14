# 1470. Shuffle the Array

def shuffle (nums,n):
    # a=[]
    # b=[]
    # new=[]
    # for x in range(0,n):
    #     a.append(nums[x])
    # for y in range(n,n*2):
    #     b.append(nums[y])
    # for z in range(0,n):
    #     new.append(a[z])
    #     new.append(b[z])
    # return new
    
    new=[]
    for i in range (n):
        new.append(nums[i])
        new.append(nums[n+i])

    return new


print(shuffle([2,5,1,3,4,7],2))