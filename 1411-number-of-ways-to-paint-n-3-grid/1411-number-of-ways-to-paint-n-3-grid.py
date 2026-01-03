MOD = 10**9 + 7
res = [12]
a121, a123 = 6, 6
for i in range(4999):
    a121, a123 = a121 * 3 + a123 * 2, a121 * 2 + a123 * 2
    res.append((a121 + a123) % MOD)
class Solution:
    def numOfWays(self, n: int) -> int:
        return res[n-1]