class Solution:
    def stoneGameV(self, A):
        n = len(A)
        if n == 1:
            return 0
        dp = [[0] * n for _ in range(n)]
        mx = [[0] * n for _ in range(n)]
        for i in range(n):
            mx[i][i] = A[i]
        for j in range(1, n):
            mid = j
            ls = A[j]
            rs = 0
            for i in range(j - 1, -1, -1):
                ls += A[i]
                while mid > i and (rs + A[mid]) * 2 <= ls:
                    rs += A[mid]
                    mid -= 1
                if rs * 2 == ls:
                    dp[i][j] = mx[i][mid]
                if mid > i:
                    dp[i][j] = max(dp[i][j],mx[i][mid - 1])
                if mid < j:
                    dp[i][j] = max(dp[i][j],mx[j][mid + 1])
                mx[i][j] = max(mx[i][j - 1],dp[i][j] + ls)
                mx[j][i] = max(mx[j][i + 1],dp[i][j] + ls)
        return dp[0][n - 1]