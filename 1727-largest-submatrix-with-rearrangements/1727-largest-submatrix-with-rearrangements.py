class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(1,n):
            for j in range(m):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
        res = 0
        for r in matrix:
            r.sort(reverse = True)
            mv = r[0]
            # print(r,mv)
            for i in range(m):
                if r[i] < mv:
                    mv = r[i]
                res = max(res,mv*(i+1))
        return res