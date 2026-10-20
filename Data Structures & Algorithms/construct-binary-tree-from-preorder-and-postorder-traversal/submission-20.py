class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pos = {v: i for i, v in enumerate(postorder)}

        def build(preL, preR, postL):
                if preL > preR:
                    return None
                root = TreeNode(preorder[preL])
                if preL == preR:
                    return root
                left_root = preorder[preL + 1]
                size = pos[left_root] - postL + 1
                root.left  = build(preL + 1, preL + size, postL)
                root.right = build(preL + size + 1, preR, postL + size)
                return root

        return build(0, len(preorder) - 1, 0)






