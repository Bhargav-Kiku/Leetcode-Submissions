class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp0 = [0] * n
        dp1 = [0] * n
        dp0[0] = dp1[0] = 1
        for i in range(1, n):
            dp0[i] = dp0[i-1]
            dp1[i] = dp1[i-1]
            if nums[i] > nums[i-1]:
                dp0[i] = dp1[i-1] + 1
            elif nums[i] < nums[i-1]:
                dp1[i] = dp0[i-1] + 1
            # print(dp0, dp1)
        return max(dp0[-1], dp1[-1])