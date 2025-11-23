# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minswaps(self,arr): #Self-Note Cycle Decomposition
        res = 0
        n = len(arr)
        ai = [(x, i) for i, x in enumerate(arr)]
        ai.sort()
        vis = [False] * n
        for i in range(n):
            if vis[i] or ai[i][1] == i: 
                continue
            c = 0
            j = i
            while not vis[j]:
                vis[j] = True
                j = ai[j][1]
                c += 1
            res += c - 1
        return res

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        arr = []
        q = deque([(root,0)])
        while q:
            n, l = q.popleft()
            if len(arr) == l:
                arr.append([])
            arr[l].append(n.val)
            if n.left:
                q.append((n.left,l+1))
            if n.right:
                q.append((n.right,l+1))
        res = 0
        for x in arr:
            res += self.minswaps(x)
        return res