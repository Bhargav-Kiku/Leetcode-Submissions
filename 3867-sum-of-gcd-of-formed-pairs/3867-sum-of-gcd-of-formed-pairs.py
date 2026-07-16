class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        pg = []
        cm = 0
        for i in nums:
            cm = max(cm, i)
            pg.append(gcd(cm, i))
        pg.sort()
        n = len(pg)
        i = 0
        j = n - 1
        res = 0
        while i < j:
            res += gcd(pg[i], pg[j])
            i += 1
            j -= 1
        return res