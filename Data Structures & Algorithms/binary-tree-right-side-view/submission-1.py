# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        res = [root.val]

        queue = [root]
        nodes_to_explore = []

        while queue:                
            # print("[", end="")
            # for n in queue:
            #     print(n.val, end=", ")
            # print("]")

            # if len(queue) == 1: res.append(queue[0].val)

            while queue:
                node = queue.pop(0)
            
                if node.left:
                    nodes_to_explore.append(node.left)

                if node.right:
                    nodes_to_explore.append(node.right)

            if not nodes_to_explore:
                break 
            
            res.append(nodes_to_explore[-1].val)
            queue = nodes_to_explore
            nodes_to_explore = []

        return res                


        