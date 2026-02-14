def twosum (l1,l2):
    n1=0
    n2=0
    for i in l1[::-1]:
        n1=n1*10+i
    for j in l2[::-1]:
        n2=n2*10+j
    n3=n1+n2
    l3=[]
    while n3!=0:
        l3.append(n3%10)
        n3=n3//10
    return l3
    



print(twosum([1,2,3],[2,3,4]))

# l1=[1,2,3]
# l1.append(2)
# print(l1)