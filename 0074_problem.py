# 74. Search a 2D Matrix

def searchMatrix(matrix,target):
    
    a= False
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if target==matrix[i][j]:
                a = True
                break
    return a


print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))