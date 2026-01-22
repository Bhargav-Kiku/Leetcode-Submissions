# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leftsum(self, root, il):
        if not root: return 0
        if not root.right and not root.left:
            if il:
                return root.val
            else:
                return 0
        return self.leftsum(root.left, True) + self.leftsum(root.right, False)
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.leftsum(root, False)