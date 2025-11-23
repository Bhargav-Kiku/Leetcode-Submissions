class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(n):
            cm = cs = 0
            for j in range(i, max(-1, i - k), -1):
                if (cm < arr[j]):
                    cm = arr[j]
                cur = cm * (i - j + 1) + dp[j]
                if cs < cur:
                    cs = cur
            dp[i+1] = cs
        return dp[n]