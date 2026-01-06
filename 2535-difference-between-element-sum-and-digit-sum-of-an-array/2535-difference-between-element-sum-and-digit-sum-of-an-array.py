class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res += i
            for x in str(i):
                res -= int(x)
        return abs(res)