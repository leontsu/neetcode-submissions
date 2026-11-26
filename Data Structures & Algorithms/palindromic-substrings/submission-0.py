class Solution:
    def countSubstrings(self, s: str) -> int:
        
        self.res = 0

        for i in range(len(s)):
            self.helper(i, i, s)

        return self.res

    def helper(self, subl, subr, s):
            
        l, r = subl, subr
        while l >= 0 and r < len(s) and s[l] == s[r]:
            self.res += 1
            l -= 1
            r += 1
        
        l, r = subl, subr + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            self.res += 1
            l -= 1
            r += 1
