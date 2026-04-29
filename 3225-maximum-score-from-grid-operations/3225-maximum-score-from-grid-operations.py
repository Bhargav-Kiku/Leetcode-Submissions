class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if m == 1:
            return 0
        col = [[0]*(n+1) for _ in range(m)]
        for j in range(m):
            for i in range(n):
                col[j][i+1] = col[j][i] + grid[i][j]
        dp = [[0]*(n+1) for _ in range(n+1)]
        pM = [[0]*(n+1) for _ in range(n+1)]
        sM = [[0]*(n+1) for _ in range(n+1)]
        for c in range(1, m):
            ndp = [[0]*(n+1) for _ in range(n+1)]
            for curr in range(n+1):
                for p in range(n+1):
                    if curr <= p:
                        gain = col[c][p] - col[c][curr]

                        ndp[curr][p] = max(
                            ndp[curr][p],
                            sM[p][0] + gain
                        )
                    else:
                        gain = col[c-1][curr] - col[c-1][p]
                        ndp[curr][p] = max(
                            ndp[curr][p],
                            sM[p][curr],
                            pM[p][curr] + gain
                        )
            for curr in range(n+1):
                pM[curr][0] = ndp[curr][0]
                for p in range(1, n+1):
                    pnlty = 0
                    if p > curr:
                        pnlty = col[c][p] - col[c][curr]
                    pM[curr][p] = max(
                        pM[curr][p-1],
                        ndp[curr][p] - pnlty
                    )
                sM[curr][n] = ndp[curr][n]
                for p in range(n-1, -1, -1):
                    sM[curr][p] = max(
                        sM[curr][p+1],
                        ndp[curr][p]
                    )
            dp = ndp
        res = 0
        for k in range(n+1):
            res = max(res, dp[0][k], dp[n][k])
        return res