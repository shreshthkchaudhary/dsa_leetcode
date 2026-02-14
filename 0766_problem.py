# 766. Toeplitz Matrix

def isToeplitzMatrix (matrix):
    a=True
    for i in range (len(matrix)-1):
        n=0
        for j in range (n,len(matrix[0])-1):
            if matrix[i][j]!=matrix[i+1][j+1]:
                a=False
                break
    return a
