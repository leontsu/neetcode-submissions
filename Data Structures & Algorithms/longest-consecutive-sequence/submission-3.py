class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)

        longest = 0
        for n in hashset:
            res = 0 
            if n-1 not in hashset:
                res += 1
                i = n + 1
                while i in hashset:
                    res += 1
                    i += 1 
                longest = max(longest, res)
        return longest