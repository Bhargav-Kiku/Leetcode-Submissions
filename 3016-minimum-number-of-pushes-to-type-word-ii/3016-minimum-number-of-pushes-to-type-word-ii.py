class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        l = sorted(c.values(), reverse = True)
        tot = 8
        cur = 1
        res = 0
        for i in l:
            res += (i * cur)
            tot -= 1
            if tot == 0:
                tot = 8
                cur += 1
        return res