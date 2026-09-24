class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)

        res = set()
        for i in range(n - 1):
            left, right = i + 1, n - 1
            while left < right:
                if nums[left] + nums[right] + nums[i] == 0:
                    res.add((nums[left], nums[right], nums[i]))
                
                if nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                
                else:
                    right -= 1
        
        return [list(i) for i in res]