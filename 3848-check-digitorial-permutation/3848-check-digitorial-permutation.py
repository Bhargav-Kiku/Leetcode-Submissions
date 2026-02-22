fact = [0] * 10
fact[0] = fact[1] = 1
for i in range(2, 10):
    fact[i] = fact[i-1] * i
class Solution:
    def getCnt(self, n):
        cnt = [0] * 10
        while n > 0:
            cnt[n % 10] += 1
            n //= 10
        return cnt
    def isDigitorialPermutation(self, n: int) -> bool:
        ts = 0
        cnt1 = self.getCnt(n)
        for i in range(10):
            ts += (cnt1[i] * fact[i])
        cnt2 = self.getCnt(ts)
        return cnt1 == cnt2