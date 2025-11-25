class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        n = 0
        if (k % 2 == 0 or k % 5 == 0): return -1
        while True:
            n = n * 10 + 1
            if n % k == 0:
                return len(str(n))