class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1: return 0
        maxP = 0

        for i in range(1, n):
            for j in range(i):
                maxP = max(maxP, prices[i] - prices[j])

        return maxP