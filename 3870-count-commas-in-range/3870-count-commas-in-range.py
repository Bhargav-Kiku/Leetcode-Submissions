res = [0] * (100001)
for i in range(1,100001):
    res[i] = res[i-1] + (len(str(i)) - 1) // 3
class Solution:
    def countCommas(self, n: int) -> int:
        return res[n]