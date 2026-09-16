MOD = 10**9 + 7
n = 1000
k = 999
dp = [[0] * (k + 1) for _ in range(n)]
for i in range(n):
    dp[i][0] = 1
for j in range(1, k + 1):
    tot = 0
    for i in range(1, n):
        tot = (tot + dp[i - 1][j - 1]) % MOD
        dp[i][j] = (dp[i - 1][j] + tot) % MOD
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        return dp[n - 1][k]