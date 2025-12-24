class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        cnt = Counter(s)
        f = {k: s.find(k) for k in cnt}
        lo = {k: s.rfind(k) for k in cnt}
        res = []
        q = deque()
        for k in cnt:
            q.appendleft([f[k], lo[k], cnt[k]])
            l, r, t = inf, -inf, 0
            for x, y, z in q:
                t += z
                l = min(l, x)
                r = max(r, y)
                if t == r - l + 1:
                    break
            if t == r - l + 1:
                res.append(s[l:r+1])
                q = deque()
        return res