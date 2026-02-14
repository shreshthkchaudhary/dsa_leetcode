# 240. Search a 2D Matrix II

def searchMatrix(matrix,target):
    # for i in range (len(matrix)):
    #     for j in range (len(matrix[i])):
    #         if matrix[i][j]==target:
    #             return True
    # return False

    for i in range (len(matrix)):
        if matrix[i][len(matrix[i])-1]==target:
            return True
        elif matrix[i][0]==target:
            return True
        elif matrix[i][len(matrix[i])-1]>target:
            for j in range (len(matrix[i])-1):
                if matrix[i][j]==target:
                    return True
    return False

print (searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5))

        