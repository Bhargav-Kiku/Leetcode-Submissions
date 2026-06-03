class Solution:
    def earliestFinishTime(self, la: List[int], lb: List[int], wa: List[int], wb: List[int]) -> int:
        maxv = 300005
        l = w = ml = mw = maxv
        n, m = len(la), len(wa)
        for i in range(n):
            l = min(l, la[i] + lb[i])
        for i in range(m):
            w = min(w, wa[i] + wb[i])
            ml = min(ml, max(wa[i], l) + wb[i])
        for i in range(n):
            mw = min(mw, max(la[i], w) + lb[i])
        return min(mw, ml)