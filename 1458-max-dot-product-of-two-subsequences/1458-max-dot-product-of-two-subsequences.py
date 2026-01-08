class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[float('-inf')] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                v = nums1[i] * nums2[j]
                cv = v
                if i > 0 and j > 0:
                    cv = max(cv, v + dp[i-1][j-1])
                if i > 0:
                    cv = max(cv, dp[i-1][j])
                if j > 0:
                    cv = max(cv, dp[i][j-1])
                dp[i][j] = cv
        return dp[n-1][m-1]