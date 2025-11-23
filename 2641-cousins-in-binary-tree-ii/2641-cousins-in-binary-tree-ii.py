# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        mp = []
        q = deque([(root,0)])
        while q:
            n, l = q.popleft()
            if len(mp) == l:
                mp.append(0)
            mp[l] += n.val
            if n.left:
                q.append((n.left,l+1))
            if n.right:
                q.append((n.right,l+1))
        root.val = 0
        q = deque([(root,0)])
        while q:
            n, l = q.popleft()
            if n.left:
                if n.right:
                    v = n.right.val + n.left.val
                    n.left.val = mp[l+1] - v
                    n.right.val = mp[l+1] - v
                    q.append((n.right,l+1))
                else:
                    v = n.left.val
                    n.left.val = mp[l+1] - v
                        
                q.append((n.left,l+1))
            elif n.right:
                v = n.right.val
                n.right.val = mp[l+1] - v
                q.append((n.right,l+1))
        return root