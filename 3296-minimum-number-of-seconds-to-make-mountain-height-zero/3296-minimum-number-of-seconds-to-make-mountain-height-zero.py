import heapq
class Solution:
    def minNumberOfSeconds(self, mh: int, wt: List[int]) -> int:
        n = len(wt)
        res = 0
        q = [(x,x,2) for x in wt]
        heapq.heapify(q)
        while mh > 0:
            w, p, t = heapq.heappop(q)
            # print(w,p,t)
            mh -= 1
            res = max(res,w)
            heapq.heappush(q,(p*((t*(t+1)//2)),p,t+1))
        return res