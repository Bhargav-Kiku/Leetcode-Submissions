class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)
        res = float('inf')
        for i in range(n):
            st = landStartTime[i]
            d = landDuration[i]
            for j in range(m):
                x, y = waterStartTime[j], waterDuration[j]
                ct = 0
                if x <= st:
                    res = min(res, max(x + y, st) + d)
                else:
                    res = min(res, max(st + d, x) + y)
        return res