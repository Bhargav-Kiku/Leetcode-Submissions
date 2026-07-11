class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        mapy = defaultdict(list)
        for i, j in edges:
            mapy[i].append(j)
            mapy[j].append(i)
        vis = [False] * n
        c = 0
        for i in range(n):
            if not vis[i]:
                comp = [i]
                c += 1
                vis[i] = True
                q = deque([i])
                while q:
                    x = q.popleft()
                    for v in mapy[x]:
                        if not vis[v]:
                            comp.append(v)
                            vis[v] = True
                            q.append(v)
                edges = 0
                for i in comp:
                    edges += len(mapy[i])
                lc = len(comp)
                if lc * (lc-1) != edges:
                    c -= 1
        return c