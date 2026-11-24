# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0

        def dfs(node, max_val=float("-inf"), prev=float("-inf")):
            nonlocal good

            if not node: return
            # max_val = max(node.val, max_val)

            dfs(node.left, max(node.val, max_val))
            dfs(node.right, max(node.val, max_val))

            if node.val >= max_val: 
                good += 1

        dfs(root)
        return good
        