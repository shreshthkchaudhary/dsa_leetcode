# 151. Reverse Words in a String

def reverseWords(s):
    s=" ".join(s.split())
    s=" "+s
    n=""
    m=len(s)
    l=len(s)
    
    for i in s[::-1]:
        l-=1
        if i.isalnum()==False:
            n+=s[l:m]
            m=l
    n=n.removeprefix(n[0])
    return n   

print(reverseWords("the sky is blue"))