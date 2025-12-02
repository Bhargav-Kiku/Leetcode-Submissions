MOD = 1000000007
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mp = defaultdict(int)
        for i, j in points:
            mp[j] += 1
        li = [x * (x - 1) // 2 for x in mp.values() if x != 1]
        tl = sum(li)
        res = 0
        for l in li:
            tl -= l
            res += l * tl
        return res % MOD