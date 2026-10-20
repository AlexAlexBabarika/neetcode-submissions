class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(pre,post):
            if not pre: return None
            node=TreeNode(pre[0])

            if len(pre)>1:
                size=post.index(pre[1])+1
                node.left=build(pre[1:size+1],post[:size])
                node.right=build(pre[size+1:],post[size:-1])

            return node
        return build(preorder,postorder)
        # if len(preorder) == 1: return preorder
        # indices = {val: idx for idx, val in enumerate(postorder)}

        # self.start = 0
        # def dfs(l, r):
        #     if l > r: 
        #         return None

        #     root_val = preorder[self.start]
        #     self.start += 1
        #     root = TreeNode(root_val)
        #     pivot = indices[root_val]

        #     # if pivot - start > 2:
        #     root.left = dfs(l + 1, r)
        #     root.right = dfs(l, pivot-1)

        #     # else:
        #     #     if pivot - start == 2:
        #     #         root.left = postorder[pivot-2]
        #     #         root.right = postorder[pivot-1]
                
        #     return root

        # return dfs(0, len(postorder) - 1)
