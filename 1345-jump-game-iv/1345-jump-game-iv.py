class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        na = [arr[0]]
        rnd = [False]
        for i in range(1,n):
            if arr[i] == na[-1]:
                rnd[-1] = True
                continue
            na.append(arr[i])
            rnd.append(False)
        # print(na)
        n = len(na)
        vis = [False] * n
        da = defaultdict(list)
        for i in range(n):
            da[na[i]].append(i)
        # print(da)
        s = deque([(0,0)])
        vis[0] = True
        while s:
            nv, c = s.popleft()
            for x in da[na[nv]][::-1]:
                if not vis[x]:
                    vis[x] = True
                    if x == n - 1:
                        return c + 1
                    s.append((x, c + 1))
            if nv - 1 >= 0 and not vis[nv - 1]:
                vis[nv - 1] = True
                s.append((nv - 1, c + 1))
            if nv + 1 < n and not vis[nv + 1]:
                vis[nv + 1] = True
                if nv + 1 == n - 1:
                    return c + 1 + rnd[nv] + rnd[nv + 1]
                s.append((nv + 1, c + 1 + rnd[nv]))
            # print(s)
            da[na[nv]].clear()
        return 0