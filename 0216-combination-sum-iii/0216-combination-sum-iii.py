class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def back(v,s,l):
            if s == n and len(l) == k:
                res.append(l[:])
                return
            if s > n or v > 9 or len(l) > k:
                return
            l.append(v)
            back(v+1,s+v,l)
            l.pop()
            back(v+1,s,l)

        back(1,0,[])
        return res