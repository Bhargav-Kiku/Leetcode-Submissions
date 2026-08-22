class Solution:
    def checkDivisibility(self, n: int) -> bool:
        ds = 0
        dp = 1
        s = str(n)
        for i in s:
            ds += int(i)
            dp *= int(i)
        ts = ds + dp
        return True if n % ts == 0 else False