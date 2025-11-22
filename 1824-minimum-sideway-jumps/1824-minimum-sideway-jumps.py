class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        dp = [float('inf')] * 4
        dp[1], dp[2], dp[3] = 1, 0, 1
        for x in obstacles:
            if x: dp[x] = float('inf')            
            for j in (1,2,3):
                if j != x:
                    dp[j] = min(dp[j], dp[(j%3)+1] + 1, dp[(j+1)%3+1] + 1)
        return min(dp[1], dp[2], dp[3])