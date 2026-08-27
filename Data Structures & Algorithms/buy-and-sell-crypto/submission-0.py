class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        r = 1
        maxP = 0

        while r < len(prices):
            if prices[left] < prices[r]:
                profit = prices[r] - prices[left]
                maxP = max(maxP, profit)
            else:
                left = r
            r += 1
        return maxP