class Solution:
    def check(self, grid, i, j):
        print(i,j)
        vis = [False] * 9
        ds = defaultdict(int)
        for k in range(i-2,i+1):
            for l in range(j-2,j+1):
                v = grid[k][l]
                if v > 9 or v < 1:
                    return False
                ds[f"row{k}"] += v
                ds[f"col{l}"] += v
                if k - l == abs(i-j):
                    ds["dia1"] += v
                if k + l == max(i, j) + min(i,j) - 2:
                    ds["dia2"] += v
                # print("Test :",k,l,v)
                if vis[v-1]:
                    # print("Here",v-1)
                    return False
                vis[v-1] = True
        # print(ds)
        if max(ds.values()) != min(ds.values()):
            return False
        return True
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        res = 0
        n, m = len(grid), len(grid[0])
        for row in grid:
            print(*row)
        for i in range(2,n):
            for j in range(2,m):
                if self.check(grid,i,j): res += 1
        return res