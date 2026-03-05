class Solution:
    def minOperations(self, s: str) -> int:
        f = True
        a = 0
        n = len(s)
        for i in s:
            if i == '1':
                if f:
                    a += 1
            else:
                if not f:
                    a += 1
            f = not f
        return min(a, n - a)