class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[[float('inf')] * (k + 1) for _ in range(m)] for _ in range(n)]
        dp[0][0][0] = 0
        for i in range(n):
            for j in range(m):
                if i != 0 or j != 0:
                    dp[i][j][0] = min(
                        dp[i-1][j][0] if i != 0 else float('inf'),
                        dp[i][j-1][0] if j != 0 else float('inf')
                    ) + grid[i][j]
        max_g = 0
        for i in range(n):
            for j in range(m):
                max_g = max(max_g, grid[i][j])
        for nt in range(1, k + 1):
            na = [float('inf') for _ in range(max_g + 1)]
            for i in range(n):
                for j in range(m):
                    na[grid[i][j]] = min(
                        na[grid[i][j]],
                        dp[i][j][nt-1]
                    )
            nna = [float('inf') for _ in range(max_g + 1)]
            nna[max_g] = na[max_g]
            for v in range(max_g - 1, -1, -1):
                nna[v] = min(
                    nna[v+1],
                    na[v]
                )
            for i in range(n):
                for j in range(m):
                    dp[i][j][nt] = min(
                        (dp[i-1][j][nt] + grid[i][j]) if i != 0 else float('inf'),
                        (dp[i][j-1][nt] + grid[i][j]) if j != 0 else float('inf'),
                        nna[grid[i][j]]
                    )
        return dp[-1][-1][k]