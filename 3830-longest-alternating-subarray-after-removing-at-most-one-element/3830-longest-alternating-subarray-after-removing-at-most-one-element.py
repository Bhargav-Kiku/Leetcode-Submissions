class Solution:
    def longestAlternating(self, nums: List[int]) -> int:
        n = len(nums)
        res = 1
        f0 = g0 = f1 = g1 = 1
        fp2 = g_ = 1
        for i in range(1, n):
            a, b = nums[i-1], nums[i]
            nf0 = ng0 = 1
            if a < b: nf0 = g0 + 1
            elif a > b: ng0 = f0 + 1
            nf1 = ng1 = 1
            if a < b: nf1 = g1 + 1
            elif a > b: ng1 = f1 + 1
            if i >= 2:
                c = nums[i - 2]
                if c < b: nf1 = max(nf1, g_ + 1)
                elif c > b: ng1 = max(ng1, fp2 + 1)
            res = max(res, nf0, ng0, nf1, ng1)
            fp2, g_ = f0, g0
            f0, g0 = nf0, ng0
            f1, g1 = nf1, ng1
        return res