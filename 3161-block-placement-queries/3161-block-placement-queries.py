class Solution:
    def __init__(self):
        self.M = 50000
        self.seg = [0] * (4 * (self.M + 1))
    def update(self, node, l, r, idx, val):
        if l == r:
            self.seg[node] = val
            return
        mid = (l + r) // 2
        if idx <= mid:
            self.update(2 * node, l, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, r, idx, val)

        self.seg[node] = max(self.seg[2 * node], self.seg[2 * node + 1])
    def query(self, node, l, r, ql, qr):
        if qr < l or ql > r:
            return 0
        if ql <= l and r <= qr:
            return self.seg[node]
        mid = (l + r) // 2
        return max(
            self.query(2 * node, l, mid, ql, qr),
            self.query(2 * node + 1, mid + 1, r, ql, qr)
        )
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        from sortedcontainers import SortedSet
        bs = SortedSet([0])
        for q in queries:
            if q[0] == 1:
                bs.add(q[1])
        pos = list(bs)
        for i in range(1, len(pos)):
            self.update(1, 0, self.M, pos[i], pos[i] - pos[i - 1])
        res = []
        for i in range(len(queries) - 1, -1, -1):
            if queries[i][0] == 2:
                x = queries[i][1]
                sz = queries[i][2]
                idx = bs.bisect_right(x) - 1
                pB = bs[idx]
                bG = self.query(1, 0, self.M, 0, pB)
                bG = max(bG, x - pB)
                res.append(bG >= sz)
            else:
                x = queries[i][1]
                idx = bs.index(x)
                lB = bs[idx - 1]
                self.update(1, 0, self.M, x, 0)
                if idx + 1 < len(bs):
                    rB = bs[idx + 1]
                    self.update(1, 0, self.M, rB, rB - lB)
                bs.remove(x)
        res.reverse()
        return res