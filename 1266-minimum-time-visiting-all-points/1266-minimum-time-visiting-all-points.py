class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        cx, cy = points[0]
        for i, j in points[1:]:
            while cx != i and cy != j:
                if cx < i:
                    cx += 1
                else:
                    cx -= 1
                if cy < j:
                    cy += 1
                else:
                    cy -= 1
                res += 1
            res += abs(cx - i) + abs(cy - j)
            # print(res)
            cx = i
            cy = j
        return res