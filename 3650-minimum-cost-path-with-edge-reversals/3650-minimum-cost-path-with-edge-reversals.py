class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for i, j, k in edges:
            adj[i].append((j,k))
            adj[j].append((i,2*k))
        vis = [float('inf')] * n
        vis[0] = 0
        q = [(0,0)]
        while q:
            nn, nc = heapq.heappop(q)
            if nc > vis[nn]:
                continue
            for x, j in adj[nn]:
                if j + nc < vis[x]:
                    vis[x] = j + nc
                    heapq.heappush(q, (x, j + nc))
        return vis[n-1] if vis[n-1] != float('inf') else -1