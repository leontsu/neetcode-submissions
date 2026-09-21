class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        window = {}
        res = 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            diff = (r - l + 1) - (max(window.values()))

            while diff > k:
                window[s[l]] -= 1
                l += 1
                diff = (r - l + 1) - (max(window.values()))

            res = max(res, (r - l + 1))

        return res
