class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        res = 0
        substring = 0

        for r in range(len(s)):
            if s[r] not in window:
                window.add(s[r])
                substring += 1
                res = max(substring, res)
            else:
                res = max(res, substring)
                while s[r] in window:
                    substring -= 1
                    window.remove(s[l])
                    l += 1
                window.add(s[r])
                substring += 1

        return res