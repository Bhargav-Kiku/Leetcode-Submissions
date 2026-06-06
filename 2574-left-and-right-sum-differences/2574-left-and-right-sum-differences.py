class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = sum(nums)
        res = [0] * n
        cs = 0
        for i in range(n):
            s -= nums[i]
            res[i] = abs(s - cs)
            cs += nums[i]
        return res