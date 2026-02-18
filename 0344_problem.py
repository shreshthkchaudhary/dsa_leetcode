# 344. Reverse String

def reverseString(s):
    n=len(s)
    for i in range(len(s)//2):
        s[i],s[n-1]=s[n-1],s[i]
        n-=1
    return s



print(reverseString(["h","e","l","l","o"]))