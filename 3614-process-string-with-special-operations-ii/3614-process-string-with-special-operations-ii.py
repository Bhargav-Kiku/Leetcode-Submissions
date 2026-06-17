class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = 0
        for c in s:
            if c == '*':
                n = max(0, n - 1)
            elif c == '#':
                n *= 2
            elif c != '%':
                n += 1
        if k >= n:
            return '.'
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if c == '*':
                n += 1
            elif c == '#':
                mid = n // 2
                if k >= mid:
                    k -= mid
                n = mid
            elif c == '%':
                k = n - 1 - k
            else:
                if k == n - 1:
                    return c
                n -= 1
        return '.'