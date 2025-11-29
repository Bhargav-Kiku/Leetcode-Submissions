class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        r = sum(nums) - nums[0]
        n = len(nums)
        l = 0
        res = [0] * n
        for i in range(n):
            res[i] = abs(l - r)
            l += nums[i]
            r -= nums[i+1] if i + 1 < n else 0
        return res