# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def recurforme(root,mxv,mnv):
            if not root:
                self.res = max(self.res,mxv-mnv)
                return
            mxv = max(mxv,root.val)
            mnv = min(mnv,root.val)
            recurforme(root.left,mxv,mnv)
            recurforme(root.right,mxv,mnv)
        recurforme(root,0,root.val)
        return self.res