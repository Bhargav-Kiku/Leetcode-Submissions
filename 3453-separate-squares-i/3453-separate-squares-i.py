class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        ta = sum((l * l for x, y, l in squares))
        es = [(y, 1, l) for x, y, l in squares] + [(y + l, 0, l) for x, y, l in squares]
        es.sort()
        cw = 0
        ca = 0
        ph = 0
        for i in range(len(es)):
            y, x, l = es[i]
            hd = y - ph
            ad = cw * hd
            if ca + ad >= ta / 2:
                oph = (ta / 2 - ca) / cw
                return ph + oph
            cw += l if x else -l
            ca += ad
            ph = y