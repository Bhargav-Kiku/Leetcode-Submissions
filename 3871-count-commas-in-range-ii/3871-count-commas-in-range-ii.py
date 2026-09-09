class Solution:
    def countCommas(self, n: int) -> int:
        res, p = 0, 1000
        while p <= n:
            res += n - p + 1
            p *= 1000
        return res