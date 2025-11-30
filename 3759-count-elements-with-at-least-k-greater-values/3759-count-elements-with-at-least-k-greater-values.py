class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 0: return n
        nums.sort()
        idx = n - k - 1
        while idx >= 0 and nums[idx] == nums[idx+1]:
            idx -= 1
        return idx+1