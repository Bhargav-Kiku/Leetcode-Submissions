class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [-1] * n
        def dfs(i):
            if dp[i] != -1:
                return dp[i]
            res = 1
            for x in range(i + 1, min(n, i + d + 1)):
                if arr[x] >= arr[i]:
                    break
                res = max(res, 1 + dfs(x))
            for x in range(i - 1, max(-1, i - d - 1), -1):
                if arr[x] >= arr[i]:
                    break
                res = max(res, 1 + dfs(x))
            dp[i] = res
            return dp[i]
        return max(dfs(i) for i in range(n))