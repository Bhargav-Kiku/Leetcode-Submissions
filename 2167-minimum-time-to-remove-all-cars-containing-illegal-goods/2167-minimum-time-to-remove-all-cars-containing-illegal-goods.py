class Solution:
    def minimumTime(self, s: str) -> int:
        c = 0
        x = 0
        for i in s:
            if i == '1':
                c += 1
            else:
                c -= 1
            if c < x:
                x = c
            if c > 0:
                c = 0
        return len(s) + x