class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * n
        for i in range(n-1, -1, -1):
            dp[i] = -float('inf')
            cur = 0
            for j in range(3):
                if i + j < n:
                    cur += stoneValue[i+j]
                    dp[i] = max(dp[i], cur - (dp[i+j+1] if i + j + 1 < n else 0))
        # print(dp)
        if dp[0] > 0:
            return "Alice"
        if dp[0] == 0:
            return "Tie"
        return "Bob"