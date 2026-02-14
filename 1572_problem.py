# 1572. Matrix Diagonal Sum

def diagonalSum(mat):
    sum=0
    l=len(mat)
    if len(mat)==1:
        return mat[0[0]]
    for i in range (l):
        sum+=mat[i][i]
        if i!=l-1:
            sum+=mat[i][l-1]
        l-=1
    return sum



print(diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))