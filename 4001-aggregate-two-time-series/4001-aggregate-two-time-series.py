class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        res = []
        n, m = len(series1), len(series2)
        i = j = 0
        c = min(series1[0][0], series2[0][0])
        while i < n or j < m:
            res.append([c, (series1[i][1] if (i < n) else 0) + (series2[j][1] if j < m else 0)])
            if i < n and series1[i][0] == c:
                i += 1
            if j < m and series2[j][0] == c:
                j += 1
            c = min(series1[i][0] if i < n else float('inf'), series2[j][0] if j < m else float('inf'))
        return res