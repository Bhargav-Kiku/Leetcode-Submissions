class Solution:
    def check(self, row, col, cells, day):
        g = [[0] * col for _ in range(row)]
        q = deque()
        for r, c in cells[:day]:
            g[r - 1][c - 1] = 1
        for i in range(col):
            if not g[0][i]:
                q.append((0, i))
                g[0][i] = -1
        while q:
            r, c = q.popleft()
            if r == row - 1:
                return True
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and g[nr][nc] == 0:
                    g[nr][nc] = -1
                    q.append((nr, nc))
        return False
    
    
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        l, r = 1, row * col
        while l < r:
            mid = r - (r - l) // 2
            if self.check(row, col, cells, mid):
                l = mid
            else:
                r = mid - 1
        return l