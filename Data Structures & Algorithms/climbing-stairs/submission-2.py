class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2: return 1
        
        p1 = 2
        p2 = 1

        for i in range(2, n):
            p1, p2 = p1 + p2, p1

        return p1
