class Solution:
    def check(self, maps, k):
        if not maps: return True
        return sum(maps.values()) - max(maps.values()) <= k
    def characterReplacement(self, s: str, k: int) -> int:
        maps = {}
        st = 0
        res = 0
        for i in s:
            if i not in maps:
                maps[i] = 1
            else:
                maps[i] += 1
            while not self.check(maps,k):
                maps[s[st]] -= 1
                if maps[s[st]] == 0:
                    del maps[s[st]]
                st += 1
            res = max(res, sum(maps.values()))
        return res