class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        N = len(nums)

        if N == 1: return nums[0]

        nums = sorted(nums)
        # print(nums)

        most_seen = nums[0]
        num_seen = 1
        for i in range(1, N):
            # print(most_seen, num_seen)
            if nums[i] != most_seen: 
                most_seen = nums[i]
                num_seen = 1

            else:
                num_seen += 1
            
            if num_seen > N // 2: return most_seen

        return -1

        # if num_seen >= N // 2: return most_seen