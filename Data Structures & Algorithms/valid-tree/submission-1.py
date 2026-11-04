class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        hashmap = {i:[] for i in range(n)}
        for n1, n2 in edges:
            hashmap[n1].append(n2)
            hashmap[n2].append(n1)

        visited = set()
        def dfs(i, prev):
            if i in visited:
                return False

            visited.add(i)
            for n in hashmap[i]:
                if n == prev:
                    continue
                if not dfs(n, i):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n