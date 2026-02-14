# 202. Happy Number

def isHappy(n):
# def loop1 ():
    m=n
    def ntoarr(m):
        arr=[]
        while m!=0:
            a=m%10
            m=m//10
            arr.append(a)
        return arr[::-1]
    
    def arrsqsum1(arr):
        arr1=[]
        for i in range(len(arr)):
            arr1.append(arr[i]**2)
        return arr1
    
    def sum1(add):
        s=0
        for j in range (len(add)):
            s+=add[j]
        return s
    
    def xinarr (arr2,x):
        for i in range(len(arr2)):
            if arr2[i]==x:
                return False
        return True
    
    def main (x):
        arr2=[]
        while True:
            if x==1:
                return True
            elif xinarr(arr2,x)==False:
                return False
            arr2.append(x)
            x=sum1(arrsqsum1(ntoarr(x)))
        
    return main(sum1(arrsqsum1(ntoarr(m))))
print(isHappy(1000000))