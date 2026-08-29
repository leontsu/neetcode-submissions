class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}

        maj = len(nums) // 2

        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1

        for k, v in hashmap.items():
            if v > maj:
                return k
                