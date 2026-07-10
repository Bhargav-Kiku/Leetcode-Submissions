lg = 18
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        nn = sorted(enumerate(nums), key=lambda x: x[1])
        gi = [0] * n
        for i, (x, y) in enumerate(nn):
            gi[x] = i
        st = [[0] * lg for _ in range(n)]
        r = 0
        for i in range(n):
            if r < i: r = i
            while (r + 1 < n and
                   nn[r + 1][1] - nn[r][1] <= maxDiff and
                   nn[r + 1][1] - nn[i][1] <= maxDiff):
                r += 1
            st[i][0] = r
        for j in range(1, lg):
            for i in range(n):
                st[i][j] = st[st[i][j - 1]][j - 1]
        res = []
        for u, v in queries:
            a, b = gi[u], gi[v]
            if a > b: a, b = b, a
            if a == b: res.append(0); continue
            c, sts = a, 0
            for j in range(lg - 1, -1, -1):
                if st[c][j] < b:
                    c = st[c][j]
                    sts += (1 << j)
            res.append(sts + 1 if st[c][0] >= b else -1)
        return res