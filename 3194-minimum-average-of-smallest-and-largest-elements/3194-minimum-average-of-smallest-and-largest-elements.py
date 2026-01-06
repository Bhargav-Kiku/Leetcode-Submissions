class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        res = (nums[0] + nums[n-1]) / 2
        for i in range(1,n//2):
            res = min(res, (nums[i] + nums[n-i-1]) / 2)
        return res