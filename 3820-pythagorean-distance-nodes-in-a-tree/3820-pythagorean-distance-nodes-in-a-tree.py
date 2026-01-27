class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        adj = defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        def bfs(x):
            dist = [-1] * n
            dist[x] = 0
            q = deque([x])
            while q:
                cn = q.popleft()
                for nn in adj[cn]:
                    # print(cn,nn)
                    if (dist[nn] == -1 or dist[nn] > dist[cn] + 1):
                        q.append(nn)
                        dist[nn] = dist[cn] + 1
            return dist
        a, b, c = bfs(x), bfs(y), bfs(z)
        # print(a, b, c)
        res = 0
        for i in range(n):
            f, g, h = sorted([a[i], b[i], c[i]])
            if ((f ** 2) + (g ** 2)) == (h ** 2):
                res += 1
        return res