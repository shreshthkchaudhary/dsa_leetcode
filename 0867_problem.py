# 867. Transpose Matrix

def transpose(matrix):
    # res=[]
    # for i in range (len(matrix[0])):
    #     temp=[]
    #     for j in range (len(matrix)):
    #         temp.append(matrix[j][i])
    #     res.append(temp)
    # return res

    ans =[[0]*len(matrix) for _ in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            ans[j][i]= matrix[i][j]
    return ans

    # # in case of square matrix
    # for i in range (0,len(matrix)-1):
    #     for j in range (i,len(matrix)):
    #         matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    # return matrix


print(transpose([[1,2,3],[4,5,6],[7,8,9]]))