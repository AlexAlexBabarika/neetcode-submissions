class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        prev1, prev2 = 0, 0

        for n in nums:
            prev1, prev2 = max(prev2 + n, prev1), prev1

        return max(prev1, prev2)