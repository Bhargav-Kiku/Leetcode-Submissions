class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ca = {}
        res = 0
        i = 0
        for j in range(len(s)):
            ca[s[j]] = ca.get(s[j], 0) + 1
            while ca[s[j]] > 2:
                ca[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        return res