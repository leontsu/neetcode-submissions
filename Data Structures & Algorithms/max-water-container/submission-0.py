class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        mostWater = 0

        while l < r:
            currWater = min(heights[l], heights[r]) * (r - l)
            mostWater = max(mostWater, currWater)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return mostWater