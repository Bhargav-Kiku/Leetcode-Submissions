class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n, m = len(grid), len(grid[0])
        dp = [[-1] * m for _ in range(n)]
        q = [(grid[0][0], 0, 0)]
        dp[0][0] = grid[0][0]
        while q:
            c, i, j = heapq.heappop(q)
            if i == n-1 and j == m-1: return c < health
            for x, y in {(-1,0), (0, -1), (1, 0), (0, 1)}:
                ni, nj = i + x, j + y
                if 0 <= ni < n and 0 <= nj < m:
                    nw = c + grid[ni][nj]
                    if dp[ni][nj] > nw or dp[ni][nj] == -1:
                        dp[ni][nj] = nw
                        heapq.heappush(q,(nw, ni, nj))