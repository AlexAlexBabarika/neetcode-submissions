# class Node:
#     def __init__(self, val, children=None):
#         self.val = val
#         self.children = children if children is not None else []

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        result = []

        def dfs(i, track):
            if i >= n: return
            if sum(track) == target:
                result.append(track.copy()) 
                return
            elif sum(track) > target:
                return

            track.append(nums[i])
            dfs(i, track.copy())
            track.pop()
            dfs(i+1, track.copy())

        arr = []
        dfs(0, arr)
        return result

