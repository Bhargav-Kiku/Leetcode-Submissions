class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        for x, y, z in queries:
            c = 0
            for i, j in points:
                if ((x-i)**2 + (y-j)**2)**(0.5) <= z:
                    c += 1
            res.append(c)
        return res