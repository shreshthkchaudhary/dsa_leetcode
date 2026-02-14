# 728. Self Dividing Numbers

def selfDividingNumbers(left,right):
    res=[]
    for i in range(left,right+1):
        arr=[]
        n=i
        while n>0:
            arr.append(n%10)
            n//=10
        arr.reverse()
        valid=True
        for j in range(len(arr)):
            if arr[j]==0 or i%arr[j]!=0:
                valid=False
                break
        if valid:    
            res.append(i)

    return res


print(selfDividingNumbers(10,100))
