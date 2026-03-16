# 73. Set Matrix Zeroes

def setZeroes(matrix):
    x=len(matrix)
    y=len(matrix[0])
    n=set()
    m=set()
    for i in range(x):
        for j in range(y):
            if matrix[i][j]==0:
                n.add(i)
                m.add(j)
    
    for i in n:
        for j in range(y):
            matrix[i][j]=0

    for i in m:
        for j in range(x):
            matrix[j][i]=0

    return matrix

print(setZeroes([[0,1,2,0],
                 [3,4,5,2],
                 [1,3,1,5]]))