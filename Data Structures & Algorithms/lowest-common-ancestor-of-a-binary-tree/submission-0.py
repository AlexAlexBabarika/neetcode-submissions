# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None
        def check(node):
            nonlocal lca

            if not node:
                return [False, False]
            
            if lca:
                return [False, False]

            left = check(node.left)
            right = check(node.right)

            foundP = left[0] or right[0] or node == p
            foundQ = left[1] or right[1] or node == q

            if foundP and foundQ and not lca:
                lca = node

            return [foundP, foundQ]

        check(root)
        return lca
