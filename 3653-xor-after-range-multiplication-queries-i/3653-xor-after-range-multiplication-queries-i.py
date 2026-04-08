mod = (10 ** 9 + 7)
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for l, r, k, v in queries:
            for i in range(l,r+1,k):
                nums[i] = (nums[i] * v) % mod
        res = 0
        for i in nums:
            res ^= i
        return res