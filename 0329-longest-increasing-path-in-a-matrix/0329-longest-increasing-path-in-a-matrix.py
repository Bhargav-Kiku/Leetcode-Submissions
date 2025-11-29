class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        vis = [[False] * m for _ in range(n)]
        @cache
        def dfs(i,j):
            vis[i][j] = True
            rm = 0
            for x, y in {(-1,0),(0,-1),(1,0),(0,1)}:
                if 0 <= i+x < n and 0 <= j+y < m and matrix[i+x][j+y] < matrix[i][j]:
                    rm = max(rm,dfs(i+x,j+y))
            return 1 + rm
        res = 0
        for i in range(n):
            for j in range(m):
                if vis[i][j] == False:
                    res = max(res, dfs(i,j))
        return res