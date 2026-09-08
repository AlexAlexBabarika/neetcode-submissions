class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        prev1, prev2 = 0, 0
        for n in range(1, len(nums)):
            prev1, prev2 = max(prev2 + nums[n], prev1), prev1

        max1 = max(prev1, prev2)
        prev1, prev2 = 0, 0

        for n in range(len(nums) - 1):
            prev1, prev2 = max(prev2 + nums[n], prev1), prev1

        max2 = max(prev1, prev2)

        return max(max1, max2)