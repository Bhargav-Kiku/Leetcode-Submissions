class Solution:
    def longestPalindrome(self, s: str) -> int:
        f = Counter(s)
        res = 0
        o = False
        for x in f.values():
            res += x
            if x & 1 == 1:
                if not o:
                    o = True
                else:
                    res -= 1
        return res