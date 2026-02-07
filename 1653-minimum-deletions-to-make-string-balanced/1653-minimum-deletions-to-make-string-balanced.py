class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        if 'a' not in s or 'b' not in s: return 0
        pre = 0
        suf = s.count('a')
        res = suf
        for i in range(n):
            if s[i] == 'a':
                suf -= 1
            else:
                pre += 1
            res = min(res, pre + suf)
        return res