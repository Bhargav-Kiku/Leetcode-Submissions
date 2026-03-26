class Solution:
    def canPartitionGrid(self, grid):
        m, n = len(grid), len(grid[0])
        tot = 0
        bot = defaultdict(int)
        top = defaultdict(int)
        left = defaultdict(int)
        right = defaultdict(int)
        for row in grid:
            for x in row:
                tot += x
                bot[x] += 1
                right[x] += 1
        sT = 0
        for i in range(m - 1):
            for j in range(n):
                val = grid[i][j]
                sT += val
                top[val] += 1
                bot[val] -= 1
            sumbot = tot - sT
            if sT == sumbot:
                return True
            diff = abs(sT - sumbot)
            if sT > sumbot:
                if self.check(top, grid, 0, i, 0, n - 1, diff):
                    return True
            else:
                if self.check(bot, grid, i + 1, m - 1, 0, n - 1, diff):
                    return True
        sL = 0
        for j in range(n - 1):
            for i in range(m):
                val = grid[i][j]
                sL += val
                left[val] += 1
                right[val] -= 1
            sR = tot - sL
            if sL == sR:
                return True
            diff = abs(sL - sR)
            if sL > sR:
                if self.check(left, grid, 0, m - 1, 0, j, diff):
                    return True
            else:
                if self.check(right, grid, 0, m - 1, j + 1, n - 1, diff):
                    return True
        return False

    def check(self, mp, grid, r1, r2, c1, c2, diff):
        rows = r2 - r1 + 1
        cols = c2 - c1 + 1
        if rows * cols == 1:
            return False
        if rows == 1:
            return grid[r1][c1] == diff or grid[r1][c2] == diff
        if cols == 1:
            return grid[r1][c1] == diff or grid[r2][c1] == diff
        return mp.get(diff, 0) > 0