class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        c = 0
        m = 10 ** 9 + 7
        f = Counter([y for x,y in points])
        b = [i * (i - 1) // 2 for i in f.values() if i >= 2]
        tb = sum(b)
        for nb in b:
            tb -= nb
            c += nb * tb
        return c % m