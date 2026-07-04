class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = [list() for _ in range(n+1)]
        for i, j, k in roads:
            g[i].append((j, k))
            g[j].append((i, k))
        q = deque([1])
        vis = [0] * (n + 1)
        vis[1] = 1
        res = float('inf')
        while q:
            u = q.popleft()
            for v, w in g[u]:
                res = min(res, w)
                if not vis[v]:
                    vis[v] = 1
                    q.append(v)
        return res