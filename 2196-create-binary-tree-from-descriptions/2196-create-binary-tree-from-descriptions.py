# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        bt = {}
        s = set()
        for i, j, k in descriptions:
            if i not in bt:
                nn = TreeNode(i)
                bt[i] = nn
            if j not in bt:
                nn = TreeNode(j)
                bt[j] = nn
            s.add(j)
            if k:
                bt[i].left = bt[j]
            else:
                bt[i].right = bt[j]
        for i in bt.keys():
            if i not in s:
                return bt[i]