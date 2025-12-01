class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def valid(m):
            e = 0
            for p in batteries:
                e += min(p, m)
            return e // n >= m
            
        l = 0
        h = sum(batteries) // n
        res = -1
        while l <= h:
            m = l + (h - l) // 2
            if valid(m):
                res = m
                l = m + 1
            else:
                h = m - 1
        return res