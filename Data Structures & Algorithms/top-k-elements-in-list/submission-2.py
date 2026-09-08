class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {} # keys: num, values: count
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1

        for c, v in hashmap.items():
            freq[v].append(c)
        
        res = []
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res