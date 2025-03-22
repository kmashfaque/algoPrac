def exist(board, word):
    if not board or not board[0]:
        return False

    rows, cols = len(board), len(board[0])

    def dfs(r, c, index):
        # Base case: If we have found the entire word
        if index == len(word):
            return True
        
        # Check if we are out of bounds or character does not match
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
            return False

        # Mark the current cell as visited (temporary change)
        temp = board[r][c]
        board[r][c] = "#"  # Placeholder to indicate visited

        # Explore four directions
        found = (dfs(r + 1, c, index + 1) or  # Down
                 dfs(r - 1, c, index + 1) or  # Up
                 dfs(r, c + 1, index + 1) or  # Right
                 dfs(r, c - 1, index + 1))    # Left

        # Backtrack: Restore the original character
        board[r][c] = temp
        return found

    # Start DFS from every cell that matches the first letter
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0] and dfs(i, j, 0):
                return True

    return False

# Example Usage
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCE"
print(exist(board, word))  # Output: True
