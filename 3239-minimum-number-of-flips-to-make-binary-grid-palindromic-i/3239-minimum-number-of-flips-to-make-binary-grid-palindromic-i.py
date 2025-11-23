class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        rc = 0
        for r in grid:
            x = 0
            y = m - 1
            while x < y:
                if r[x] != r[y]:
                    rc += 1
                x += 1
                y -= 1
        cc = 0
        for j in range(m):
            x = 0
            y = n - 1
            while x < y:
                if grid[x][j] != grid[y][j]:
                    cc += 1
                x += 1
                y -= 1
        return min(rc,cc)