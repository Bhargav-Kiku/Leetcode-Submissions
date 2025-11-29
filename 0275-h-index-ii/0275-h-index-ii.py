class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        h = len(citations)-1
        n = h + 1
        if citations[-1] == 0: return 0
        res = 0
        while l <= h:
            m = l + (h - l) // 2
            t = (n - m)
            v = citations[m]
            if v >= t:
                res = t
                h = m - 1
            else:
                l = m + 1
        return res