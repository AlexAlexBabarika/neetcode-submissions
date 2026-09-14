# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkHeight(root: Optional[TreeNode]) -> int:
            if root is None: return 0

            left = checkHeight(root.left)
            if left == -1:
                return -1

            right = checkHeight(root.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1 

            return 1 + max(left, right)

        return checkHeight(root) != -1
        