class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        if len(nums) == 0:
            return 0

        l, r = 0, len(nums) - 1

        while l < r:
            while l < r and nums[r] == val:
                r -= 1
            if nums[l] == val:
                temp = nums[r]
                nums[r] = nums[l]
                nums[l] = temp
            l += 1
         
        return l if nums[l] == val else l + 1