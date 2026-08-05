class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = {i: [] for i in range(n)}
        for src, dst in invocations:
            g[src].append(dst)
        q = [k]
        vis = set([k])
        while q:
            sus = q.pop()
            for next in g[sus]:
                if next not in vis:
                    vis.add(next)
                    q.append(next)
        res = []
        for x in range(n):
            if x in vis:
                continue
            for next in g[x]:
                if next in vis:
                    return list(range(n))
            res.append(x)
        return res