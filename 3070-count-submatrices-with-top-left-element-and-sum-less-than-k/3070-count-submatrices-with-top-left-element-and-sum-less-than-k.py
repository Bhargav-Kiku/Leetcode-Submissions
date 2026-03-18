class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        pg = [x[:] for x in grid]
        n = len(grid)
        m = len(grid[0])
        res = 0
        for i in range(n):
            for j in range(1, m):
                pg[i][j] += pg[i][j-1]
        for i in range(1, n):
            for j in range(m):
                pg[i][j] += pg[i-1][j]
        for i in range(n):
            for j in range(m):
                if pg[i][j] <= k:
                    res += 1
        return res