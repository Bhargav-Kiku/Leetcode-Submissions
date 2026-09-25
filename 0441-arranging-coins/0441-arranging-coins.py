class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 0
        h = 10**6
        res = 0
        while l <= h:
            mid = (l + h) // 2
            if ((mid * (mid + 1)) // 2) <= n:
                res = mid
                l = mid + 1
            else:
                h = mid - 1
        return res