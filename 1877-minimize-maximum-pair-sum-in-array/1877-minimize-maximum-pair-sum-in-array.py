class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums) - 2
        res = nums[0] + nums[-1]
        i = 1
        while i < n:
            res = max(res, nums[i] + nums[n])
            i += 1
            n -= 1
        return res