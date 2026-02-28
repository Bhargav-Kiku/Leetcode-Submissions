MOD = 1000000007
res = [0] * (100001)
res[1] = 1
for i in range(2, 100001):
    res[i] = int(bin(res[i-1])[2:] + bin(i)[2:], 2) % MOD

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return res[n]