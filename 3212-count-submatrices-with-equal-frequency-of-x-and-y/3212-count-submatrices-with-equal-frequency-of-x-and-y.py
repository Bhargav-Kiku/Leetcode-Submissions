class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        g = [[0] * m for _ in range(n)]
        isT = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] != '.' or (isT[i-1][j] if i > 0 else False) or (isT[i][j-1] if j > 0 else False):
                    isT[i][j] = True
                if grid[i][j] == 'X':
                    g[i][j] = 1
                elif grid[i][j] == 'Y':
                    g[i][j] = -1
        res = 0
        for i in range(n):
            for j in range(1, m):
                g[i][j] += g[i][j-1]
        for i in range(1, n):
            for j in range(m):
                g[i][j] += g[i-1][j]
        for i in range(n):
            for j in range(m):
                if isT[i][j] and g[i][j] == 0:
                    res += 1
        return res