# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root,p):
            if not root:
                return 0
            l = dfs(root.left,root)
            r = dfs(root.right,root)
            self.res += abs(l) + abs(r)
            return root.val - 1 + l + r
        dfs(root,None)
        return self.res