class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            e = set()
            o = set()
            for j in range(i,n):
                if nums[j] & 1: o.add(nums[j])
                else: e.add(nums[j])
                if len(e) == len(o):
                    if j - i + 1 > res:
                        res = j - i + 1
        return res