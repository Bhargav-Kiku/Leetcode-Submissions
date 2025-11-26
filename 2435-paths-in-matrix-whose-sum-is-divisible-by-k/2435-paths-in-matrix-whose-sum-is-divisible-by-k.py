MOD = 1000000007
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[[0] * k for _ in range(m+1)] for _ in range(n+1)]
        dp[1][1][grid[0][0] % k] = 1
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0: continue
                v = grid[i][j] % k
                for q in range(k):
                    f, s = dp[i+1][j][(k+q-v) % k], dp[i][j+1][(k+q-v) % k]
                    # print(i,j,q,v,f,s,k+q-v)
                    dp[i+1][j+1][q] = ((f) + (s)) % MOD
        # for r in dp:
        #     print(r)
        return dp[-1][-1][0]