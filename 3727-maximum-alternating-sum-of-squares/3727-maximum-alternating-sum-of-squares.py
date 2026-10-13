class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = [i ** 2 for i in nums]
        nums.sort()
        n = len(nums)
        return sum(nums[n//2:]) - sum(nums[:n//2])