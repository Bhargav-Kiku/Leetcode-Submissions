class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        res = 0
        n, m = len(grid), len(grid[0])
        for i in range(n-2):
            for j in range(m-2):
                c = 0
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        if x == i + 1 and (y == j or y == j + 2): continue
                        c += grid[x][y]
                if c > res:
                    res = c
        return res