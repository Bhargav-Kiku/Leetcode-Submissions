class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z = s.count('0')
        if z == 0:
            return 0
        if k == n:
            return 1 if z == n else -1
        if (k % 2 == 0) and (z % 2 == 1):
            return -1
        o = n - z
        def ok(t):
            total = t * k
            if (total & 1) != (z & 1):
                return False
            oddMax = t if (t & 1) else (t - 1)
            evenMax = (t - 1) if (t & 1) else t
            if oddMax < 1:
                return False
            L = max(z, total - o * evenMax)
            R = min(z * oddMax, total)
            if L > R:
                return False
            if (L & 1) != (z & 1):
                L += 1
            return L <= R
        t = (z + k - 1) // k
        if t < 1:
            t = 1
        upper = 2 * n + 5
        if k % 2 == 1:
            if (t & 1) != (z & 1):
                t += 1
            while t <= upper:
                if ok(t):
                    return t
                t += 2
        else:
            while t <= upper:
                if ok(t):
                    return t
                t += 1
        return -1