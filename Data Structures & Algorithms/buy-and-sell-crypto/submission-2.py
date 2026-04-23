class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1
        maxP = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            if prices[l] > prices[r]:
                l = r
            else:
                r += 1
            maxP = max(maxP, profit)
        return maxP
            
        