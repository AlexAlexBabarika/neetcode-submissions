from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cnt = Counter(nums)

        for num in cnt:
            if cnt[num] > 1: return num

        return -1