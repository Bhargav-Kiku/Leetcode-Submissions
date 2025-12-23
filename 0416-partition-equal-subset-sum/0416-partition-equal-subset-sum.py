class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1: return False
        t = s // 2
        dp = [False] * (t + 1)
        dp[0] = True
        for i in nums:
            if i > t:
                break
            for j in range(t,-1,-1):
                if dp[j]:
                    if j + i <= t:
                        dp[j+i] = True
        # print(dp)
        return dp[-1]