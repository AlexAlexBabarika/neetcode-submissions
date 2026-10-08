class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(idx, cur):
            if len(cur) == n:
                res.append(cur.copy())
                return

            for i in range(n):
                if nums[i] in cur: continue
                cur.append(nums[i])
                dfs(i, cur)
                cur.pop()

        for i in range(n):
            dfs(i, [nums[i]])
        return res



        