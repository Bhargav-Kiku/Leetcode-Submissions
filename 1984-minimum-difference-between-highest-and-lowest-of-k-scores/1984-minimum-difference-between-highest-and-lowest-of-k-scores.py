class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        j = k-1
        res = nums[j] - nums[i]
        for j in range(k, n):
            i += 1
            res = min(res, nums[j] - nums[i])
        return res