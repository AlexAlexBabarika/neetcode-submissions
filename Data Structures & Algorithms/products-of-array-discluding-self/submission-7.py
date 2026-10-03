class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_cnt = 0
        output = [0] * len(nums)

        for num in nums:
            if num == 0:
                zero_cnt += 1
                if zero_cnt > 1: return output

            else: 
                prod *= num

        for i in range(len(nums)):
            if zero_cnt:
                if nums[i] == 0:
                    output[i] = prod
                    # zero_cnt -= 1
                    # prod = 0

                else:
                    output[i] = 0

            else:
                output[i] = prod // nums[i]

        return output
