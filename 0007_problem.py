# 7. Reverse Integer

def reverse(x):
    res=0
    if x>=0:
        while x!=0:
            res=res*10+x%10
            x=x//10
        if -2**31>res or res>2**31-1:
            return 0
        return res
    elif x<0:
        x*=-1
        while x!=0:
            res=res*10+x%10
            x=x//10
        if -2**31>res or res>2**31-1:
            return 0
        return res*-1

print(reverse(1534236469))