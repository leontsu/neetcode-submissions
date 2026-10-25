class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(r, c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            
            while q:
                row, col = q.popleft()
                directions = [[1,0], [0,1], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if (r in range(rows) and
                        c in range(cols) and
                        (r, c) not in visited and
                        grid[r][c] == "1"):
                        q.append((r,c))
                        visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1
        
        return islands