class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        rs = {}
        cs = {}
        q = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    rs[i] = rs.get(i,0) + 1
                    cs[j] = cs.get(j,0) + 1
                    q.append((i,j))
        res = len(q)
        for i, j in q:
            if rs[i] == 1 and cs[j] == 1:
                res -= 1
        return res