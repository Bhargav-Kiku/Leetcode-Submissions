# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def back(node, l):
            if not node.left and not node.right:
                res.append('->'.join(l))
                return
            if node.left:
                l.append(str(node.left.val))
                back(node.left,l)
                l.pop()
            if node.right:
                l.append(str(node.right.val))
                back(node.right,l)
                l.pop()
        back(root,[str(root.val)])
        return res