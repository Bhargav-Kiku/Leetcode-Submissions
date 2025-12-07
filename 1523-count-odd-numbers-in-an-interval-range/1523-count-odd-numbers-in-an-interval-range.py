class Solution:
    def countOdds(self, low: int, high: int) -> int:
        v = high - low + 1
        if high & 1:
            if v & 1 == 0:
                v //= 2
            else:
                v = (v//2) + 1
        else:
            if v & 1 == 0:
                v //= 2
            else:
                v = (v//2)
        return v