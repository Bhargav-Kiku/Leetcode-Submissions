class Solution:
    def integerReplacement(self, n: int) -> int:
        res = 0
        while n != 1:
            if n & 1:
                if n == 3 or n % 4 == 1:
                    n -= 1
                else:
                    n += 1
            else:
                n >>= 1
            res += 1
        return res