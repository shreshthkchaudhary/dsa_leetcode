# 125. Valid Palindrome

def isPalindrome(s):
    new_s=""
    for i in s:
        if i.isalnum():
            new_s+=i.lower()
    return new_s==new_s[::-1]



print(isPalindrome("A man, a plan, a canal: Panama"))