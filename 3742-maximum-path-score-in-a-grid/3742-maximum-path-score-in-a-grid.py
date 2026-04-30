class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[[-1] * (k + 1) for _ in range(m)] for _ in range(n)]
        dp[0][0] = [0] * (k + 1)
        for i in range(n):
            for j in range(m):
                for x in range(k + 1):
                    if grid[i][j] != 0:
                        if x + 1 > k: continue
                        if i > 0 and dp[i-1][j][x] != -1:
                            dp[i][j][x + 1] = dp[i-1][j][x] + grid[i][j]
                        if j > 0 and dp[i][j-1][x] != -1:
                            dp[i][j][x + 1] = max(dp[i][j][x + 1], dp[i][j-1][x] + grid[i][j])
                    else:
                        if i > 0 and dp[i-1][j][x] != -1:
                            dp[i][j][x] = dp[i-1][j][x]
                        if j > 0 and dp[i][j-1][x] != -1:
                            dp[i][j][x] = max(dp[i][j][x], dp[i][j-1][x])
        return max(dp[-1][-1])