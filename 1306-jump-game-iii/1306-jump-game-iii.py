class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        vis = [False] * n
        vis[start] = True

        def dfs(idx):
            vis[idx] = True
            if arr[idx] == 0:
                return True
            v = idx - arr[idx]
            if 0 <= v < n and not vis[v]:
                f = dfs(v)
                if f:
                    return f
            v = idx + arr[idx]
            if 0 <= v < n and not vis[v]:
                return dfs(v)
            return False
        
        return dfs(start)