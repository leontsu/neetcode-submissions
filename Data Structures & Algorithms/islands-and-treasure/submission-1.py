class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def bfs(r,c):
            if (r not in range(rows) or
                c not in range(cols) or
                (r,c) in visited or
                grid[r][c] == -1):
                return

            q.append([r,c])
            visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append([r,c])

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)
            dist += 1