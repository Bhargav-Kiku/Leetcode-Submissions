class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        dp = [1] * n
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if all(x[i] <= x[j] for x in strs):
                    dp[i] = max(dp[i], 1 + dp[j])
        return n - max(dp)