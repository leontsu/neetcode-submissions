class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows, cols = len(board), len(board[0])
        visited = set()
        notValid = set()

        # iterate through each element on the edges
            # call dfs: if any elements are connected, mark as not valid
        # read through all inner elements in the board
            # if valid and O, change to X

        def dfs(r, c, prevValue):
            if (r not in range(rows) or
                c not in range(cols) or
                (r,c) in visited or
                board[r][c] == "X"):
                return

            visited.add((r,c))
            notValid.add((r,c))
            dire = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for dr, dc in dire:
                row, col = dr + r, dc + c
                dfs(row, col, board[r][c])

        for r in range(rows):
            dfs(r, 0, board[r][0])
            dfs(r, cols - 1, board[r][cols - 1])

        for c in range(cols):
            dfs(0, c, board[0][c])
            dfs(rows - 1, c, board[rows - 1][c])

        for r in range(rows):
            for c in range(cols):
                if ((r,c) not in notValid and 
                    board[r][c] == "O" and
                    r != 0 and r != rows - 1 and
                    c != 0 and c != cols - 1):
                    board[r][c] = "X"

        