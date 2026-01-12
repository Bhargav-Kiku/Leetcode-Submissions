class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        cx, cy = points[0]
        for i, j in points[1:]:
            res += max(abs(cx-i),abs(cy-j))
            cx = i
            cy = j
        return res