class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        maps = defaultdict(list)
        for i, j, k in meetings:
            maps[k].append((i,j))
        vis = [False] * (n)
        vis[0] = vis[firstPerson] = True
        for t in sorted(maps.keys()):
            nl = defaultdict(list)
            for i, j in maps[t]:
                nl[i].append(j)
                nl[j].append(i)
            s = set()
            for i, j in maps[t]:
                if vis[i]:
                    s.add(i)
                if vis[j]:
                    s.add(j)
            q = deque(s)
            while q:
                nn = q.popleft()
                for x in nl[nn]:
                    if not vis[x]:
                        vis[x] = True
                        q.append(x)                
        res = []
        for i in range(n):
            if vis[i]:
                res.append(i)
        return res