# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ids = {}  # FIX: node -> unique id, so duplicate values become distinct tokens

        pre_str = ""
        def preorder(node):
            nonlocal pre_str

            if not node: return
            ids[node] = len(ids)
            pre_str += ',' + str(node.val) + ':' + str(ids[node])
            preorder(node.left) 
            preorder(node.right) 

        inord_str = ""
        def inorder(node):
            nonlocal inord_str

            if not node: return
            inorder(node.left) 
            inord_str += ',' + str(node.val) + ':' + str(ids[node])
            inorder(node.right)

        preorder(root) 
        inorder(root)

        return pre_str + '|' + inord_str 
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        pre_str, inord_str = data.split('|')
        if not pre_str and not inord_str: return None

        pre_l, inord_l = pre_str.split(','), inord_str.split(',')

        if len(pre_l) > 0 and pre_l[0] == '': pre_l.pop(0)
        if len(inord_l) > 0 and inord_l[0] == '': inord_l.pop(0)

        def build(pre, inord):
            if not pre and not inord: return None
            root = TreeNode(int(pre[0].split(':')[0]))
            middle = inord.index(pre[0])

            root.left = build(pre[1:middle+1], inord[:middle])
            root.right = build(pre[middle+1:], inord[middle+1:])

            return root
        
        root = build(pre_l, inord_l)
        return root