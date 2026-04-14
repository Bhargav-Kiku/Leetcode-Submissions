class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        n, m = len(robot), len(factory)
        inf = float('inf')
        dp = [[inf]*(m+1) for _ in range(n+1)]
        for j in range(m+1):
            dp[0][j] = 0
        for j in range(1, m+1):
            p, lim = factory[j-1]
            for i in range(n+1):
                dp[i][j] = dp[i][j-1]
                d = 0
                for k in range(1, min(lim, i)+1):
                    d += abs(robot[i-k] - p)
                    dp[i][j] = min(dp[i][j], dp[i-k][j-1] + d)
        return dp[n][m]