class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashmap = {}

        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1

        i = 0
        if hashmap.get(0) is not None:
            for _ in range(hashmap[0]):
                nums[i] = 0
                i += 1
        if hashmap.get(1) is not None:
            for _ in range(hashmap[1]):
                nums[i] = 1
                i += 1
        if hashmap.get(2) is not None:
            for _ in range(hashmap[2]):
                nums[i] = 2
                i += 1

        
