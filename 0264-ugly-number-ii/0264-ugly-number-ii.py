heap = []
for i in {2,3,5}:
    heapq.heappush(heap,i)
res = [1]
vis = set()
while len(res) < 1690:
    v = heapq.heappop(heap)
    res.append(v)
    for i in {2,3,5}:
        t = v * i
        if t not in vis:
            vis.add(t)
            heapq.heappush(heap,t)

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        return res[n-1]