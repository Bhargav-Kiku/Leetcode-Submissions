# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recur(root):
            if not root: return 0, True
            l, fl = recur(root.left)
            if not fl: return 0, False
            r, fr = recur(root.right)
            if not fr: return 0, False
            if abs(l - r) > 1: return 0, False
            return max(l, r) + 1, True
        _, res = recur(root)
        return res