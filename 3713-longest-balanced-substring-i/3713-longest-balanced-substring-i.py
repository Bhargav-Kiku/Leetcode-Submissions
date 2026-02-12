class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 1
        for i in range(n):
            maps = Counter()
            for j in range(i,n):
                maps[s[j]] += 1
                if min(maps.values()) == max(maps.values()):
                    res = max(res, j - i + 1)
        return res