# 1351. Count Negative Numbers in a Sorted Matrix

def countNegatives(grid):
    # count=0
    # for i in range(len(grid)):
    #     for j in range(len(grid[i])):
    #         if grid[i][j] < 0:
    #             count+=1
    # return count


    count=0
    for i in range(len(grid)):
        for j in range(len(grid[i])-1,-1,-1):
            if grid[i][j] < 0:
                count+=1
            elif grid[i][j] >= 0:
                break
    return count


print(countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))