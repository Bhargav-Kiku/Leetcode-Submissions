class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = Counter(s)
        for i in t:
            s[i] -= 1
            if s[i] == -1:
                return i