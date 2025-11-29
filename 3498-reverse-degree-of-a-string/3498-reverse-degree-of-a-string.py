class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i, x in enumerate(s):
            res += ((i + 1) * (26 - (ord(x) - ord('a'))))
        return res