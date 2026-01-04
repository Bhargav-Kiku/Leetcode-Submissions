yes = {}
for i in range(1,100001):
    c = set()
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            if j * j == i:
                c.add(j)
            else:
                c.add(j)
                c.add(i // j)
        if len(c) > 4:
            break
    if len(c) == 4:
        yes[i] = c
        
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            if i in yes:
                res += sum(yes[i])
        return res