class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1

        for n in nums:
            totalProduct *= n
        
        res = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] != 0:
                res[i] = totalProduct // nums[i]
            else:
                tProduct = 1
                for j in range(len(nums)):
                    if i != j:
                        tProduct *= nums[j]
                res[i] = tProduct
        return res