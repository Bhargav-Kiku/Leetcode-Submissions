class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        c = 0
        for i in gain:
            c += i
            res = max(res, c)
        return res