class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return False

        numssum = sum(nums)
        if numssum % 2 != 0: return False

        target = numssum // 2
        sums = set()
        sums.add(0)

        for i in range(n - 1, 0, -1):
            toadd = []
            for elem in sums:
                if elem + nums[i] == target: return True
                toadd.append(elem + nums[i])

            for cand in toadd:
                sums.add(cand)

        print(sums)

        return False
        