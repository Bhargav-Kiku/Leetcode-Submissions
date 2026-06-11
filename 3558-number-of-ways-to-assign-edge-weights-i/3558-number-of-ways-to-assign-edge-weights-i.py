class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges)+1
        t = [list() for _ in range(n+1)]
        for i, j in edges:
            t[i].append(j)
            t[j].append(i)
        via = set([1])
        q = deque([(1,0)])
        l = 0
        while q:
            node, cl = q.popleft()
            if cl > l:
                l = cl
            for nxt in t[node]:
                if nxt not in via:
                    via.add(nxt)
                    q.append((nxt,cl+1))
        # print(l)
        return pow(2,l-1,1000000007)