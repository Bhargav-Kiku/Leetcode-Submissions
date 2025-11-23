class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j - 1]
        count = 0
        for c1 in range(n):
            for c2 in range(c1, n):
                psm = {0: 1}
                s = 0
                for r in range(m):
                    s += matrix[r][c2] - (matrix[r][c1 - 1] if c1 > 0 else 0)
                    count += psm.get(s - target, 0)
                    psm[s] = psm.get(s, 0) + 1
        return count