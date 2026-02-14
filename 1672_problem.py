# 1672. Richest Customer Wealth

def maximumWealth(accounts):
    n=len(accounts)
    for i in range(n):
        sum=0
        m=len(accounts[i])
        for j in range(m):
            sum=sum+accounts[i][j]
        accounts[i]=sum
    return max(accounts)

print(maximumWealth([[1,2,3,4],
                     [5,6,7,8],
                     [9,10,11,12],
                     [13,14,15,16],
                     [17,18,19,20]]))