class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        p1 = 0
        for i in range(n):
            p1 += (i * nums[i])
        res = p1
        for i in range(1, n):
            p1 = (p1 - s + (n * nums[i-1]))
            res = max(res, p1)
        return res