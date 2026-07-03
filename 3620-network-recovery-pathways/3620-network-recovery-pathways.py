class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        ind = [0] * n
        for u, v, w in edges:
            g[u].append((v, w))
            ind[v] += 1
        q = deque()
        for i in range(n):
            if ind[i] == 0:
                q.append(i)
        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in g[u]:
                ind[v] -= 1
                if ind[v] == 0:
                    q.append(v)
        def check(limit):
            INF = 10 ** 30
            dp = [INF] * n
            dp[0] = 0
            for u in topo:
                if dp[u] == INF:
                    continue
                if u != 0 and u != n - 1 and not online[u]:
                    continue
                for v, w in g[u]:
                    if w < limit:
                        continue
                    if v != n - 1 and not online[v]:
                        continue
                    if dp[u] + w < dp[v]:
                        dp[v] = dp[u] + w
            return dp[-1] <= k
        left = 0
        right = 10 ** 9
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans