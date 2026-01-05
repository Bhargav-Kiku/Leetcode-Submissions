class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        s = 0
        c = 0
        mneg = float('inf')
        for i in matrix:
            for j in i:
                if j < 0:
                    c += 1
                s += abs(j)
                mneg = min(mneg, abs(j))
        if c & 1:
            return s - 2 * mneg
        return s