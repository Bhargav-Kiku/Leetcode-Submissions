class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        res = nums[0]
        nums[0] = 51
        nums.sort()
        return res + sum(nums[0:2])