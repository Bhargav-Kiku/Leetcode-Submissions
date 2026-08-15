class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        if sum(nums) == 0:
            return 0
        xr = 0
        for i in nums:
            xr ^= i
        return len(nums) if xr else len(nums) - 1