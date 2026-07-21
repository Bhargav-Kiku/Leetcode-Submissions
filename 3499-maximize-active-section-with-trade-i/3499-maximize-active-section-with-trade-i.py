class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        res = 0
        l = 0
        c = 0
        for i in range(n):
            if s[i] == '0':
                c += 1
            else:
                if l != 0 and c != 0:
                    res = max(res, c + l)
                if c != 0:
                    l = c
                    c = 0
        if l != 0 and c != 0:
            res = max(res, l + c)
        return s.count('1') + res