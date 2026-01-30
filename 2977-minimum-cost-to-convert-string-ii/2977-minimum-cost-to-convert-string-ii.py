class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        g = defaultdict(dict)
        dc = {}
        for u, v, c in zip(original, changed, cost):
            g[u][v] = min(c, g[u].get(v, inf))

        def cc(source, target):
            if source in dc:
                return dc[source].get(target, inf)
            heap, memo = [(0, source)], {source: 0}
            while heap:
                c, w = heappop(heap)
                if c == memo[w]:
                    for n, cn in g[w].items():
                        nc = cn + c
                        if nc < memo.get(n, inf):
                            memo[n] = nc
                            heappush(heap, (nc, n))
            dc[source] = memo
            return memo.get(target, inf)

        n = len(source)
        set_l = sorted({*map(len, original)})
        # print(set_l)
        dp = [inf] * (n + 1)
        dp[0] = 0
        for s in range(n):
            if dp[s] == inf:
                continue
            if source[s] == target[s]:
                dp[s + 1] = min(dp[s + 1], dp[s])
            for l in set_l:
                e = s + l
                if e > n:
                    break
                r = source[s:e]
                if r in g:
                    dp[e] = min(dp[e], dp[s] + cc(r, target[s:e]))
        return dp[-1] if dp[-1] != inf else -1