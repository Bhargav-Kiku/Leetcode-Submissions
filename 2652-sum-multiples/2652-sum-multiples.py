div = [False] * (1001)
for i in {3,5,7}:
    j = i
    while j <= 1000:
        div[j] = True
        j += i
pre = []
l = 0
for i in range(1001):
    pre.append(l + (i if div[i] else 0))
    l = pre[-1]
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return pre[n]