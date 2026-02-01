class Solution:
    def longestAlternating(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, 0] for _ in range(n)]
        dp[0] = [1, 1]
        for i in range(1, n):
            if nums[i-1] < nums[i]: 
                dp[i][0] = dp[i-1][1]+1
                dp[i][1] = 1
            elif nums[i-1] > nums[i]: 
                dp[i][1] = dp[i-1][0]+1
                dp[i][0] = 1
            else: 
                dp[i][1] = 1
                dp[i][0] = 1
        dp2 = [[0, 0] for _ in range(n)]
        dp2[-1] = [1, 1]
        for i in range(n-2, -1, -1):
            if nums[i+1] < nums[i]: 
                dp2[i][0] = dp2[i+1][1]+1
                dp2[i][1] = 1
            elif nums[i+1] > nums[i]: 
                dp2[i][1] = dp2[i+1][0]+1
                dp2[i][0] = 1
            else:
                dp2[i][1] = 1
                dp2[i][0] = 1
        a, b = max(max(dp[i]) for i in range(n)), max(max(dp2[i]) for i in range(n))
        res = max(a, b)
        for i in range(1, n-1):
            l, r = nums[i-1], nums[i+1]
            if l > r: res = max(res, dp[i-1][0]+dp2[i+1][1])
            elif l < r: res = max(res, dp[i-1][1]+dp2[i+1][0])
        return res