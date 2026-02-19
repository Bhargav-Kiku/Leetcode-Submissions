class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        p = 0
        st = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]: st += 1
            else:
                p = st
                st = 1
            if st <= p: res += 1
        return res
