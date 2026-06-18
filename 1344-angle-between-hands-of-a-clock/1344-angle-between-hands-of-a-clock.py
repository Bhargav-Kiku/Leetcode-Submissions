class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        mh = minutes * 6
        hh = ((hour % 12) * 30) + (minutes / 2)
        a, b = max(mh, hh), min(mh, hh)
        return min(a - b, ((b - a) % 360))