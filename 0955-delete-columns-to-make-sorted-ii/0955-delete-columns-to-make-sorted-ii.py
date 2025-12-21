class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        dp = [False] * (len(strs) - 1)
        res = 0
        for c in zip(*strs):
            if all(dp[i] or c[i] <= c[i+1] for i in range(len(c) - 1)):
                for i in range(len(c) - 1):
                    if c[i] < c[i+1]:
                        dp[i] = True
            else:
                res += 1
        return res