class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: # fresh
                    fresh += 1
                if grid[r][c] == 2: # rotten
                    visited.add((r,c))
                    q.append([r,c])
        
        def discover(r,c):
            nonlocal fresh

            if (r not in range(rows) or
                c not in range(cols) or
                (r,c) in visited or
                grid[r][c] != 1):
                return

            visited.add((r,c))
            grid[r][c] = 2
            fresh -= 1
            q.append((r,c))

        time = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                discover(r - 1, c)
                discover(r + 1, c)
                discover(r, c + 1)
                discover(r, c - 1)
            time += 1

        return time if fresh == 0 else -1