class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        cs = bottom
        maps = defaultdict(list)
        for a in allowed:
            maps[a[:2]].append(a[2])
        def letsrecur(cs):
            if len(cs) == 1:
                return True
            ns = ""
            q = [ns]
            nq = []
            for i in range(1,len(cs)):
                v = cs[i-1:i+1]
                # print(v)
                if v in maps:
                    for x in maps[v]:
                        for j in q:
                            nq.append(j+x)
                    q = nq
                    nq = []
                else:
                    return False
            # print(nq)
            # print(q)
            for x in q:
                if letsrecur(x):
                    return True
            return False
        return letsrecur(cs)