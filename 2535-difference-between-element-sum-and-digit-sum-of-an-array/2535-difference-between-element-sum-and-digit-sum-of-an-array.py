class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            while i > 0:
                res += i % 10
                i //= 10
        return sum(nums) - res