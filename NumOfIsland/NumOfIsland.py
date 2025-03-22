def numOfIsland(board):
    if not board:
        return 0
    
    rows, cols = len(board), len(board[0])
    num_Island = 0

    def dfs(r,c):
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] == "0":
            return 

        board[r][c] = "0"
        
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == "1":
                dfs(i,j)
                num_Island += 1
    
    return num_Island


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(grid[0][1])
print(numOfIsland(grid))
    