class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        cur = []
        def dfs(openn, closen):
            if openn == closen == n:
                res.append("".join(cur))
                return

            if openn < n:
                cur.append("(")
                dfs(openn + 1, closen)
                cur.pop()

            if closen < openn:
                cur.append(")")
                dfs(openn, closen + 1)
                cur.pop()

        dfs(0,0)
        return res