class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        # for r in mat:
        #     print(*r)
        # print()
        nmat = [[0] * n for _ in range(m)]
        for i in range(m):
            sc = 0
            for j in range(n):
                sc += mat[i][j]
                nmat[i][j] += sc
                if i > 0:
                    nmat[i][j] += nmat[i-1][j]
        # for r in nmat:
        #     print(*r)
        # print()
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                mnr, mxr = max(0, i - k), min(m - 1, i + k)
                mnc, mxc = max(0, j - k), min(n - 1, j + k)
                res[i][j] = nmat[mxr][mxc]
                if mnr > 0:
                    res[i][j] -= nmat[mnr-1][mxc]
                if mnc > 0:
                    res[i][j] -= nmat[mxr][mnc-1]
                if mnr > 0 and mnc > 0:
                    res[i][j] += nmat[mnr-1][mnc-1]
        return res