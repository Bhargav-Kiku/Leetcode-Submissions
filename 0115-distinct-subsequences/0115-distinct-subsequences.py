class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        mapy = defaultdict(list)
        n = len(t)
        for i in range(n):
            mapy[t[i]].append(i+1)
        dp = [0] * (n+1)
        for i in s:
            for j in sorted(mapy[i],reverse=True):
                if dp[j-1] > 0:
                    dp[j] += dp[j-1]
                if j == 1:
                    dp[j] += 1
        return dp[-1]