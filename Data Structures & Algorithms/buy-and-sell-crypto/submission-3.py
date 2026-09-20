class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            curProfit = prices[r] - prices[l]

            if curProfit < 0:
                l = r
                r += 1
            else:
                maxProfit = max(maxProfit, curProfit)
                r += 1

        return maxProfit