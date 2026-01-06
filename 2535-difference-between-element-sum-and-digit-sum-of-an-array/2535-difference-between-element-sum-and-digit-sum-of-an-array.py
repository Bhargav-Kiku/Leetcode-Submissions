class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res += i
            while i > 0:
                res -= i % 10
                i //= 10
        return res