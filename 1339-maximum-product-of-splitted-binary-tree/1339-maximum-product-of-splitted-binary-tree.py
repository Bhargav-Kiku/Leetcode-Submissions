# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def inorder(node):
            if not node:
                return 0
            l = inorder(node.left)
            r = inorder(node.right)
            return node.val + l + r
        s = inorder(root)
        def check(node):
            if not node:
                return 0
            l = check(node.left)
            r = check(node.right)
            v = node.val + l + r
            self.res = max(self.res, (v * (s - v)))
            return v
        check(root)
        return self.res % (1000000007)