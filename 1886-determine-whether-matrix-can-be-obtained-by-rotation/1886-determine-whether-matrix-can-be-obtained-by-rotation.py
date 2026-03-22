class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = m = len(mat)
        def rotate(grid):
            ng = [x[:] for x in grid]
            for i in range(n):
                for j in range(m):
                    ng[i][j] = grid[j][n - i - 1]
            return ng
        if target == mat: return True
        ng = rotate(mat)
        if target == ng: return True
        ng = rotate(ng)
        if target == ng: return True
        ng = rotate(ng)
        return target == ng