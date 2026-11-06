# class Node:
#     def __init__(self, val, children=None):
#         self.val = val
#         self.children = children if children is not None else []

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, track):
            s = sum(track)
            if s > target or i >= len(nums): return
            if s == target:
                result.append(track.copy())
                return

            track.append(nums[i])
            dfs(i, track)
            track.pop()
            dfs(i + 1, track)

        arr = []
        dfs(0, arr)
        return result

