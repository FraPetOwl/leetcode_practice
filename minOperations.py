def minimumOperations(grid: list[list[int]]) -> int:
    sum = 0 #initialize what we need to return - the sum of +1 operations
    # iterate of columns
    for j in range(len(grid[0])):
        prev = -1
        for i in range(len(grid)):
            cur = grid[i][j]
            sum+= max((1+prev) - cur,0)
            prev = max(cur, prev+1)
    return sum

print(minimumOperations([[3,2],[1,3],[3,4],[0,1]]))

# solution was not that clear - re go over in notebook / pencil