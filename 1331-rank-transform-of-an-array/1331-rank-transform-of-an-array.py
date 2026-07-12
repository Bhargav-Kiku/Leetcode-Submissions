class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        sa = sorted((x, i) for i, x in enumerate(arr))
        n = len(arr)
        res = [0] * n
        l = sa[0][0]
        r = 1
        for i in range(n):
            if sa[i][0] != l:
                l = sa[i][0]
                r += 1
            res[sa[i][1]] = r
        return res