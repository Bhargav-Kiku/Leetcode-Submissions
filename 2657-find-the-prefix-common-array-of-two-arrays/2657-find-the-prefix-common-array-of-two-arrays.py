class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ma = set()
        mb = set()
        res = []
        l = 0
        n = len(A)
        for k in range(n):
            i, j = A[k], B[k]
            ma.add(i)
            if i in mb:
                l += 1
            mb.add(j)
            if j in ma:
                l += 1
            res.append(l)
        return res