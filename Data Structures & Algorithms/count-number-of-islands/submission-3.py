class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def bfs(r,c):
            if ((r,c) in visited or
                r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == "0"):
                return False

            visited.add((r,c))

            bfs(r + 1, c)
            bfs(r - 1, c)
            bfs(r, c - 1)
            bfs(r, c + 1)

            return True

        for r in range(rows):
            for c in range(cols):
                if bfs(r,c):
                    islands += 1
        
        return islands