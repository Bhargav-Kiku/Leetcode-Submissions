class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        r = [0] * n
        c = [0] * m
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    r[i] += 1
                    c[j] += 1
        
        res = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1 and r[i] == 1 and c[j] == 1:
                    res += 1
        return res