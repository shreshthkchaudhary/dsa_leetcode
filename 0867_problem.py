# 867. Transpose Matrix

def transpose(matrix):
    res=[]
    for i in range (len(matrix[0])):
        temp=[]
        for j in range (len(matrix)):
            temp.append(matrix[j][i])
        res.append(temp)
    return res

print(transpose([[1,2,3],[4,5,6],[7,8,9]]))