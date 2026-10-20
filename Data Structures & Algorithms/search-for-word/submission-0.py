class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        
        def dfs(i, j, wcount):

            if wcount >= len(word):
                return True

            visited[i][j] = True

            if i - 1 >= 0 and visited[i-1][j] == False and board[i - 1][j] == word[wcount]:
                # top
                if dfs(i - 1, j, wcount + 1):
                    return True
            if i + 1 < len(board) and visited[i+1][j] == False and board[i + 1][j] == word[wcount]:
                # bottom
                if dfs(i + 1, j, wcount + 1):
                    return True
            if j + 1 < len(board[0]) and visited[i][j+1] == False and board[i][j + 1] == word[wcount]:
                # right
                if dfs(i, j + 1, wcount + 1):
                    return True
            if j - 1 >= 0 and visited[i][j-1] == False and board[i][j - 1] == word[wcount]:
                # left
                if dfs(i, j - 1, wcount + 1):
                    return True

            visited[i][j] = False
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1):
                        return True

        return False