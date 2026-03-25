class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        rs = [0] * n
        cs = [0] * m
        ts = 0
        for i in range(n):
            for j in range(m):
                rs[i] += grid[i][j]
                cs[j] += grid[i][j]
                ts += grid[i][j]
        if ts & 1: return False
        ts //= 2
        s = 0
        for i in range(n-1):
            s += rs[i]
            if s == ts:
                return True
            elif s > ts:
                break
        s = 0
        for i in range(m-1):
            s += cs[i]
            if s == ts:
                return True
            elif s > ts:
                break
        return False