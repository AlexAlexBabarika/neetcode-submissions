# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        # if p.val < root.val < q.val: return root
        # elif p.val < root.val and q.val < root.val:
        #     self.lowestCommonAncestor(root.left, p, q)
        # elif p.val > root.val and q.val > root.val:
        #     self.lowestCommonAncestor(root.right, p, q)
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr

        return curr