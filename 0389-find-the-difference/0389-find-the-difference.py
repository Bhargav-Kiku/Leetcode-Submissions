class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = Counter(s)
        for i in t:
            if s[i] == 0:
                return i
            s[i] -= 1