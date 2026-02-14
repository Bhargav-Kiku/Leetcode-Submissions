class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * (100) for _ in range(100)]
        rdp = [[0] * (100) for _ in range(100)]
        if poured == 0: return 0
        dp[0][0] = (poured - 1) / 2
        rdp[0][0] = 1
        for i in range(1,100):
            for j in range(i+1):
                dp[i][j] = (dp[i-1][j]) + (dp[i-1][j-1] if j > 0 else 0)
                rdp[i][j] = min(dp[i][j], 1)
                dp[i][j] = max(0, dp[i][j] - 1) / 2
        # for x in dp: print(*x)
        return rdp[query_row][query_glass]