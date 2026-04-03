class Solution:
    def maxWalls(self, rb: List[int], distance: List[int], ws: List[int]) -> int:
        n = len(rb)
        l = [0] * n
        r = [0] * n
        ar = [0] * n
        rtd = {}
        for i in range(n):
            rtd[rb[i]] = distance[i]
        rb.sort()
        ws.sort()
        for i in range(n):
            p1 = bisect.bisect_right(ws, rb[i])
            if i >= 1:
                l_bound = max(rb[i] - rtd[rb[i]], rb[i - 1] + 1)
                l_p = bisect.bisect_left(ws, l_bound)
            else:
                l_p = bisect.bisect_left(ws, rb[i] - rtd[rb[i]])
            l[i] = p1 - l_p
            if i < n - 1:
                r_bound = min(rb[i] + rtd[rb[i]], rb[i + 1] - 1)
                r_p = bisect.bisect_right(ws, r_bound)
            else:
                r_p = bisect.bisect_right(ws, rb[i] + rtd[rb[i]])
            p2 = bisect.bisect_left(ws, rb[i])
            r[i] = r_p - p2
            if i == 0:
                continue
            p3 = bisect.bisect_left(ws, rb[i - 1])
            ar[i] = p1 - p3
        sub_l, sub_r = l[0], r[0]
        for i in range(1, n):
            current_l = max(sub_l + l[i],sub_r - r[i - 1] + min(l[i] + r[i - 1], ar[i]),)
            current_r = max(sub_l + r[i], sub_r + r[i])
            sub_l, sub_r = current_l, current_r
        return max(sub_l, sub_r)