class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum(nums[i] ** 2 if len(nums) % (i+1) == 0 else 0 for i in range(len(nums)))