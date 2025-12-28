class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        l = 0
        r = m - 1
        res = 0
        for i in range(n):
            l = 0
            r = min(r, m - 1)
            while l <= r:
                mid = (l + r) // 2
                if grid[i][mid] < 0:
                    r = mid - 1
                else:
                    l = mid + 1
            r += 1
            res += r
            if r == 0:
                break
        return n * m - res
        