class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        rc = 0
        for i in range(n):
            for j in range(m//2):
                if grid[i][j] != grid[i][m-j-1]:
                    rc += 1
        cc = 0
        for j in range(m):
            for i in range(n//2):
                if grid[i][j] != grid[n-i-1][j]:
                    cc += 1
        return min(rc,cc)