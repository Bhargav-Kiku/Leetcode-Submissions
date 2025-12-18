class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        res = 0
        s = set(nums)
        for i in nums:
            if (i + diff) in s and (i + diff + diff) in s:
                res += 1
        return res