class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]: return 0
        n, m = len(grid), len(grid[0])
        q = deque()
        ng = [[-1] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ng[i][j] = 0
                    q.append((i, j, 0))
        while q:
            i, j, c = q.popleft()
            for x, y in {(-1, 0), (0, -1), (1, 0), (0, 1)}:
                ni, nj = i + x, j + y
                if 0 <= ni < n and 0 <= nj < m and (ng[ni][nj] == -1 or ng[ni][nj] > c + 1):
                    ng[ni][nj] = c + 1
                    q.append((ni, nj, c + 1))
        threat = [[-1] * m for _ in range(n)]
        threat[0][0] = ng[0][0]
        heap = [(-ng[0][0], 0, 0)]
        while heap:
            c, i, j = heapq.heappop(heap)
            threat[i][j] = -c
            if i == n-1 and j == m-1:
                return -c
            for x, y in {(-1, 0), (0, -1), (1, 0), (0, 1)}:
                ni, nj = i + x, j + y
                if not (0 <= ni < n and 0 <= nj < m):
                    continue
                new_safe = min(-c, ng[ni][nj])
                if (threat[ni][nj] == -1 or new_safe > threat[ni][nj]):
                    threat[ni][nj] = new_safe
                    heapq.heappush(heap, (-new_safe, ni, nj))