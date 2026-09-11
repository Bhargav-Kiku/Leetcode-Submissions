class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        self.res = 0
        f = Counter(digits)
        vis = set()
        def recur(idx,cur):
            if idx == 3:
                if cur not in vis:
                    self.res += 1
                return
            for i, x in f.items():
                if x != 0:
                    if idx == 0 and i == 0: continue
                    if idx == 2 and i & 1: continue
                    cur = cur * 10 + i
                    f[i] -= 1
                    recur(idx+1,cur)
                    f[i] += 1
        recur(0,0)
        return self.res