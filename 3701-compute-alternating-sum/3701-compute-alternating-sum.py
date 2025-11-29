class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if i & 1:
                res -= nums[i]
            else:
                res += nums[i]
        return res