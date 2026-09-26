class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target <= matrix[i][len(matrix[i]) - 1]:
                res = self.binarySearch(matrix[i], target)
                if res == -1:
                    return False
                else:
                    return True
        return False

        
    def binarySearch(self, nums, target) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return -1