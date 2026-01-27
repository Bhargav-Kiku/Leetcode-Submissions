class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        res = 0
        for b in range(50, -1, -1):
            if k == 0: break
            if b < k:
                res |= (1 << b)
                k -= 1
            else:
                c = comb(b, k)
                if n > c:
                    res |= (1 << b)
                    n -= c
                    k -= 1
        return res