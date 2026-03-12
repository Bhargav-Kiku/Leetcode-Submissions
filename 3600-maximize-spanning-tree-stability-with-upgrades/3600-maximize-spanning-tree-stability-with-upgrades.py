class UnionFind:
    def __init__(self, n: int) -> None:
        self.rank = [1] * n
        self.root = [i for i in range(n)]

    def find(self, x: int) -> int:
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_x] = root_y
            self.rank[root_y] += 1
        return True

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        iu = UnionFind(n)
        min_s = inf
        for u, v, s, must in edges:
            if not must: continue
            min_s = min(min_s, s)
            if not iu.union(u, v):
                return -1
        def check(min_stability: int) -> bool:
            if min_stability > min_s:
                return False
            uf = UnionFind(n)
            uf.rank, uf.root = iu.rank[:], iu.root[:]
            up = []
            for u, v, s, must in edges:
                if must: continue
                if s >= min_stability:
                    uf.union(u, v)
                elif s * 2 >= min_stability:
                    up.append((u, v))
            r = k
            for u, v in up:
                if uf.is_connected(u, v): continue
                if not r: return False
                uf.union(u, v)
                r -= 1            
            return all(uf.find(i) == uf.find(0) for i in range(n))
        left, right = -1, max(s for _, _, s, _ in edges) * 2
        while left < right:
            mid = left + (right - left + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left