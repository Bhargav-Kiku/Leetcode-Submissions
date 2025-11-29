class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rs = s[::-1]
        cs = s + '#' + rs
        pt = self.buildTree(cs)
        pl = pt[-1]
        suf = rs[: len(s) - pl]
        return suf + s

    def buildTree(self, s: str) -> list:
        n = len(s)
        pt = [0] * n
        l = 0
        for i in range(1,n):
            while l > 0 and s[i] != s[l]:
                l = pt[l - 1]
            if s[i] == s[l]:
                l += 1
            pt[i] = l
        return pt