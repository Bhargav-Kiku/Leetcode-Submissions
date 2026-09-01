class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])
        idx = [[-1] * n for _ in range(m)]
        k = 0
        sr = 0
        sc = 0
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr = r
                    sc = c
                elif classroom[r][c] == 'L':
                    idx[r][c] = k
                    k += 1
        if k == 0:
            return 0
        total_M = (1 << k) - 1
        dp = [
            [
                [-1] * (1 << k)
                for _ in range(n)
            ]
            for _ in range(m)
        ]
        q = deque()
        dp[sr][sc][0] = energy
        q.append((sr, sc, 0, energy, 0))
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            r, c, M, e, moves = q.popleft()
            for dr, dc in dir:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                if classroom[nr][nc] == 'X':
                    continue
                ne = e - 1
                if ne < 0:
                    continue
                nM = M
                if classroom[nr][nc] == 'R':
                    ne = energy
                if classroom[nr][nc] == 'L':
                    nM |= 1 << idx[nr][nc]
                if nM == total_M:
                    return moves + 1
                if ne <= dp[nr][nc][nM]:
                    continue
                dp[nr][nc][nM] = ne
                q.append((nr, nc, nM, ne, moves + 1))
        return -1