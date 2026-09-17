class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        maxLeft = []
        maxRight = [0] * len(height)
        minHeight = []
        
        maxleft = 0
        for i in range(len(height)):
            maxleft = max(maxleft, height[i])
            maxLeft.append(maxleft)

        
        maxright = 0
        for i in range(len(height) - 1, -1, -1):
            maxright = max(maxright, height[i])
            maxRight[i] = maxright

        for i in range(len(height)):
            minHeight.append(min(maxLeft[i], maxRight[i]))

        for i in range(len(minHeight)):
            res += (minHeight[i] - height[i])

        return res