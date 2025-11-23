# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(root,p):
            if not root:
                return 0
            l = dfs(root.left,root)
            r = dfs(root.right,root)
            c = l + r
            x = root.val - 1
            if p != None: p.val += x
            c += abs(x)
            return c
        return dfs(root,None)