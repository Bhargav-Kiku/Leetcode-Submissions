class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        tr = [[] for _ in range(n)]
        ind = [0] * n
        for u, v in hierarchy:
            u -= 1
            v -= 1
            tr[u].append(v)
            ind[v] += 1
        root = 0
        for i in range(n):
            if ind[i] == 0:
                root = i
                break

        INF = -10 ** 15
        capb = [0] * n
        def cap(u):
            s = present[u]
            for v in tr[u]:
                s += cap(v)
            capb[u] = min(budget, s)
            return s
        cap(root)
        dp0 = [None] * n
        dp1 = [None] * n
        def merge(a, b):
            la = len(a) - 1
            lb = len(b) - 1
            total = min(budget, la + lb)
            c = [INF] * (total + 1)
            for i in range(min(la, total) + 1):
                ai = a[i]
                if ai == INF:
                    continue
                maxj = min(lb, total - i)
                for j in range(maxj + 1):
                    bj = b[j]
                    if bj == INF:
                        continue
                    val = ai + bj
                    if val > c[i + j]:
                        c[i + j] = val
            return c
        def dfs(u):
            for v in tr[u]:
                dfs(v)
            sk = [INF] * (capb[u] + 1)
            sk[0] = 0
            bs = [INF] * (capb[u] + 1)
            bs[0] = 0
            for v in tr[u]:
                sk = merge(sk, dp0[v])
                bs = merge(bs, dp1[v])
            def comp(p):
                price = present[u] // 2 if p else present[u]
                profit = future[u] - price
                maximize = sk[:]
                if price <= capb[u]:
                    for b in range(price, capb[u] + 1):
                        if bs[b - price] != INF:
                            can = bs[b - price] + profit
                            if can > maximize[b]:
                                maximize[b] = can
                return maximize
            dp0[u] = comp(0)
            dp1[u] = comp(1)
        dfs(root)
        return max(dp0[root])
