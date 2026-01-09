# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getTree(self, node):
        if not node:
            return 0, None
        l, lt = self.getTree(node.left)
        r, rt = self.getTree(node.right)
        if l > r:
            return 1 + l, lt
        elif l < r:
            return 1 + r, rt
        return 1 + l, node
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.getTree(root)[1]