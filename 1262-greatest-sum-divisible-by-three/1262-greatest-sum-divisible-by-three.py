class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [float('-inf')] * 3
        dp[0] = 0
        for i in nums:
            ndp = dp[:]
            v = i % 3
            for k in range(3):
                ndp[k] = max(ndp[k],dp[(k-v+3) % 3] + i)
            # print(ndp)
            dp = ndp[:]
        return dp[0]