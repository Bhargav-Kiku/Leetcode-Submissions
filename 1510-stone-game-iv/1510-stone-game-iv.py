pos = []
for i in range(1, int(100000 ** 0.5) + 1):
    val = i * i
    pos.append(val)

dp = [False] * (100001)
for i in range(100001):
    if dp[i]: continue
    for j in pos:
        if i + j < 100001:
            dp[i + j] = True

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        return dp[n]