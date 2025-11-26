class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        n = len(s1)
        if n != len(s2):
            return False
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1,n):
            l = self.isScramble(s1[:i],s2[:i])
            l1 = self.isScramble(s1[-i:],s2[:i])
            r = self.isScramble(s1[i:],s2[i:])
            r1 = self.isScramble(s1[:-i],s2[i:])
            if (l and r) or (l1 and r1):
                return True
        return False