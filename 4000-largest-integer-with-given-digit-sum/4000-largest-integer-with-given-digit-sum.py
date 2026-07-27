class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        res = 0
        for _ in range(n):
            res = res * 10 + min(s, 9)
            s -= 9
            if s < 0:
                s = 0
        if s:
            return -1
        return res