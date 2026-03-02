class Solution:
    def minSwaps(self, grid):
        n = len(grid)
        z = []
        for row in grid:
            c = 0
            for j in range(n - 1, -1, -1):
                if row[j] == 0:
                    c += 1
                else:
                    break
            z.append(c)
        res = 0
        for i in range(n):
            need = n - i - 1
            j = i
            while j < n and z[j] < need:
                j += 1
            if j == n:
                return -1
            while j > i:
                z[j], z[j - 1] = z[j - 1], z[j]
                j -= 1
                res += 1
        return res