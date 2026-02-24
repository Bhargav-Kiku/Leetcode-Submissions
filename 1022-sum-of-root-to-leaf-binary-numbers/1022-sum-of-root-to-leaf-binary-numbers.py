# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def recur(node, c):
            if not node:
                return
            if not node.left and not node.right:
                self.res += (c << 1) | node.val
                return
            recur(node.right, (c << 1) | (node.val))
            recur(node.left, (c << 1) | (node.val))
        recur(root,0)
        return self.res