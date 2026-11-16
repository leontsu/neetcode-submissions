class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)

        l, r = len(dp) - 2, len(dp) - 1
        dp[l], dp[r] = 1, 1 
        while l > 0:
            dp[l - 1] = dp[l] + dp[r]
            l -= 1
            r -= 1

        return dp[l]

