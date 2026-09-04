class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()

        for n in nums:
            hashset.add(n)

        res = 0
        for n in nums:
            count = 1
            if n - 1 not in hashset:
                i = n
                while i+1 in hashset:
                    count += 1
                    i += 1
            res = max(res, count)

        return res