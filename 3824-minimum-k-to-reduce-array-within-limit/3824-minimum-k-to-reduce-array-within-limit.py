class Solution:
    def minimumK(self, nums: List[int]) -> int:
        l = 1
        h = sum(nums)
        res = 0
        while l <= h:
            m = l + (h - l) // 2
            c = sum([((x+m)//m if x % m != 0 else x//m) for x in nums])
            if c <= m * m:
                res = m
                h = m - 1
            else:
                l = m + 1
        return res