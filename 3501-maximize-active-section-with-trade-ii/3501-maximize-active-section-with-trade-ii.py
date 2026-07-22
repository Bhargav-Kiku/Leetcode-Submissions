class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0]*self.n +arr +[0]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])
            
    def query(self, low, high):
        l, r, res = low + self.n, high + self.n, 0
        while l < r:
            if l & 1:
                res = max(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = max(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        zs = [(m.end() - 1, m.start()) for m in re.finditer(r'0+',s)]
        res = [s.count('1')] *len(queries)
        st = SegTree([sum(starmap(sub, pair))+2 for pair in pairwise(zs)])
        for i, (l, r) in enumerate(queries):
            lz, rz = bisect_left(zs, (l, 0)), bisect_left(zs, (r, 0))
            rz -= (rz >= len(zs)) or (r < zs[rz][1])
            if rz > lz:
                res[i] += max(zs[lz][0] - max(l, zs[lz][1]) + min(r, zs[lz+1][0]) - zs[lz+1][1] + 2, zs[rz-1][0] - max(l, zs[rz-1][1]) + min(r, zs[rz][0]) - zs[rz][1] + 2, st.query(lz+1, rz-1) )
        return  res
        