class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float("inf")
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            
            mid = (left + right) // 2
            res = min(res, nums[mid])
            if nums[mid] < nums[left]:
                right = mid - 1
            else:
                left = mid + 1

        return res