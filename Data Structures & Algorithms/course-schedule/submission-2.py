class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        hashmap = {i:[] for i in range(numCourses)}
        for n1, n2 in prerequisites:
            hashmap[n1].append(n2)

        visited = set()
        def dfs(n):
            if n in visited:
                return False
            if hashmap[n] == []:
                return True

            visited.add(n)
            for i in hashmap[n]:
                if not dfs(i):
                    return False

            visited.remove(n)
            hashmap[n] = []

            return True
            
        
        for n in range(numCourses):
            if not dfs(n):
                return False

        return True