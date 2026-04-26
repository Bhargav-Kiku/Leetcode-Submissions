class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        vis = [[False] * m for _ in range(n)]
        def dfs(i, j, px, py):
            vis[i][j] = True
            for x, y in {(1, 0), (0, 1), (-1, 0), (0, -1)}:
                i2 = i + x
                j2 = j + y
                if 0 <= i2 < n and 0 <= j2 < m and ((i2,j2) != (px, py)) and grid[i2][j2] == grid[i][j]:
                    if vis[i2][j2]: return True
                    if dfs(i2, j2, i, j): return True
            return False
        for i in range(n):
            for j in range(m):
                if not vis[i][j]:
                    if dfs(i, j, i, j): return True
        return False