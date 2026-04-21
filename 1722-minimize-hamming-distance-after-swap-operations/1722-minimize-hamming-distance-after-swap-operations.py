class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        adj = [list() for _ in range(n)]
        for i, j in allowedSwaps:
            adj[i].append(j)
            adj[j].append(i)
        vis = [False] * n
        res = 0
        def dfs(node, r1, r2):
            r1[source[node]] += 1
            r2[target[node]] += 1
            vis[node] = True
            for x in adj[node]:
                if not vis[x]:
                    dfs(x, r1, r2)
        for i in range(n):
            if not vis[i]:
                r1 = defaultdict(int)
                r2 = defaultdict(int)
                dfs(i,r1,r2)
                # print(r1, r2)
                for x, y in r1.items():
                    res += max(y - r2[x], 0)
        return res