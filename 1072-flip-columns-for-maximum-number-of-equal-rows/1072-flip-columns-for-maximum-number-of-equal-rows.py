class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m = len(matrix[0])
        v = 1 << m - 1
        mp = {}
        for row in matrix:
            p = ''.join(map(str, row))
            op = ''.join([(str(1-x)) for x in row])
            mp[p] = mp.get(p,0) + 1
            mp[op] = mp.get(op,0) + 1
        return max(mp.values())