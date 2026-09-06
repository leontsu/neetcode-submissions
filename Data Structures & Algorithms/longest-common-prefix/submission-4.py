class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []

        for j in range(0,len(strs[0])):
            for i in range(1,len(strs)):
                if j > len(strs[i]) - 1 or strs[0][j] != strs[i][j]:
                    return "".join(res)
            res.append(strs[0][j])

        return "".join(res)