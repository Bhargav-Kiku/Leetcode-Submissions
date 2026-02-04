class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        res = a = b = c = float('-inf')
        p = nums[0]
        for i in range(1, len(nums)):
            cur = nums[i]
            na = nb = nc = float('-inf')
            if cur > p:
                na = max(a, p) + cur
                nc = max(b, c) + cur
            elif cur < p:
                nb = max(a, b) + cur
            a, b, c = na, nb, nc
            res = max(res, c)
            p = cur
        return res