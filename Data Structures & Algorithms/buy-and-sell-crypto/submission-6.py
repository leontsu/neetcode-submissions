class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l, r = 0, 1

        while r < len(prices):
            profit = prices[r] - prices[l]
            if prices[l] > prices[r]:
                l = r
                r += 1
            elif prices[r] >= prices[l]:
                r += 1
                res = max(res, profit)
            

        return res