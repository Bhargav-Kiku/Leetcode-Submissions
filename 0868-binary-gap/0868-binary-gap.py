class Solution:
    def binaryGap(self, n: int) -> int:
        s = bin(n)[2:]
        res = 0
        l = 0
        for i in range(1, len(s)):
            if s[i] == '1':
                res = max(res, i - l)
                l = i
        return res