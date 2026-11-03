class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        hashmap = { i : [] for i in range(n)}
        for a, b in edges:
            hashmap[a].append(b)
            hashmap[b].append(a)

        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            for i in hashmap[node]:
                if i == prev:
                    continue
                if not dfs(i, node):
                    return False
            return True

        return dfs(0, -1) and n == len(visited)