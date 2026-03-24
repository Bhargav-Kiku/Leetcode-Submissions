class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        cur = 1
        n, m = len(grid), len(grid[0])
        c = 0
        ng = [[0] * m for _ in range(n)]
        p = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] % 12345 == 0:
                    c += 1
                    if c > 1:
                        return ng
                    p.append((i,j))
                else:
                    cur = (cur * grid[i][j])
        if c == 1:
            ng[p[0][0]][p[0][1]] = (cur) % 12345
            return ng
        for i in range(n):
            for j in range(m):
                ng[i][j] = (cur // grid[i][j]) % 12345
        return ng