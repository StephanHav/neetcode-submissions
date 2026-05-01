class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        r = 1
        while r < len(prices):
            current = prices[r] - prices[l]
            if current > 0:
                profit = max(profit, current)
                r += 1
            else:
                l = r
                r += 1

        return profit