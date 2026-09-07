MOD = 10**9 + 7
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        tot = 0
        dp = [0] * 26
        for c in s:
            c = ord(c) - 97
            temp = tot + 1 - dp[c]
            tot = (tot + temp) % MOD
            dp[c] = (dp[c] + temp) % MOD
        return tot 