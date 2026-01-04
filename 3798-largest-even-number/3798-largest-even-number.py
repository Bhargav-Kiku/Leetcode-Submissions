class Solution:
    def largestEven(self, s: str) -> str:
        n = len(s)
        for i in range(n-1,-1,-1):
            if int(s[i]) & 1 == 0:
                return s[:i+1]
        return ""