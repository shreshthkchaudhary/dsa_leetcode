# 172. Factorial Trailing Zeroes

def trailingZeroes (n):
    a=1
    for i in range(1,n+1):
        a*=i
    n=0
    while a%10==0:
        n+=1
        a=a//10
    return n

print(trailingZeroes(5))