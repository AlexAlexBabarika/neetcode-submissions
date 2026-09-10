class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1: return 0
        maxP = [0] * n
        minP = [0] * n

        minP[0] = prices[0]

        for i in range(1, n):
            minP[i] = min(minP[i-1], prices[i])
            maxP[i] = max(prices[i] - minP[i-1], maxP[i-1])

        print(maxP)
        print(minP)

        return maxP[-1]