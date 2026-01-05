class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        s = 0
        c = 0
        z = False
        mneg = float('inf')
        for i in range(n):
            for j in range(n):
                s += abs(matrix[i][j])
                if matrix[i][j] < 0:
                    c += 1
                mneg = min(mneg, abs(matrix[i][j]))
        if c & 1:
            return s - 2 * mneg
        return s