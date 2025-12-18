class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets == 1: return 0
        t = minutesToTest // minutesToDie
        t += 1
        test = t
        res = 1
        while test < buckets:
            test *= t
            res += 1
        return res