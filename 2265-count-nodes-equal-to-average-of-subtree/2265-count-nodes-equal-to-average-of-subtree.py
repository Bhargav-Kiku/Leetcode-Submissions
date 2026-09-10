# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.res = 0
        def subtree(node):
            s = node.val
            c = 1
            if node.left:
                x, y = subtree(node.left)
                s += x
                c += y
            if node.right:
                x, y = subtree(node.right)
                s += x
                c += y
            if s // c == node.val:
                # print(node.val)
                self.res += 1
            return s, c
        subtree(root)
        return self.res