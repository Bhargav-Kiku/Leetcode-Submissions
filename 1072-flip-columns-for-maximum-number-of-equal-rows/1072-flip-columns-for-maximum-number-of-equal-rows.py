class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m = len(matrix[0])
        v = 1 << m - 1
        mp = {}
        for row in matrix:
            if row[0] == 0:
                op = tuple([1-x for x in row])
            else:
                op = tuple(row)
            mp[op] = mp.get(op,0) + 1
        return max(mp.values())