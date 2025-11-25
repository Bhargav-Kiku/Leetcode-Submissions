class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        n = 0
        c = 1
        if (k % 2 == 0 or k % 5 == 0): return -1
        while True:
            n = n * 10 + 1
            n = n % k 
            if n == 0:
                return c
            c += 1