class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        
        for i in range(2, n + 1):
            option_a = dp[i - 1] + cost[i - 1]
            option_b = dp[i - 2] + cost[i - 2]
            
            dp[i] = min(option_a, option_b)
            
        return dp[n]