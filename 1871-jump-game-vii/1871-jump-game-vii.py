class Solution:
    def canReach(self, s: str, minJ: int, mj: int) -> bool:
        n = len(s)
        if int(s[-1]): return False
        dp = [False] * n
        dp[0] = True
        r, mr = 0, mj
        for i in range(minJ, n):
            if i > mr: return False
            r += dp[i - minJ]
            if i > mj:
                r -= dp[i - mj - 1]
            if r and not int(s[i]):
                dp[i] = True
                mr = i + mj
        return r > 0