# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        queue = [root]
        res = []

        while queue:
            vals = []
            children = []
            for n in queue: vals.append(n.val)
            
            for n in queue:
                if n.left: children.append(n.left)
                if n.right: children.append(n.right)

            queue = children
            res.append(vals)

        return res


            
                
