class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        res = 1
        n, m = len(grid), len(grid[0])
        rm = [x[:] for x in grid]
        cm = [x[:] for x in grid]
        for _ in range(n):
            for i in range(1,m):
                rm[_][i] += rm[_][i-1]
        for i in range(1,n):
            for _ in range(m):
                cm[i][_] += cm[i-1][_]
        for i in range(n):
            for j in range(m):
                for t in range(1,min(n-i,m-j)):
                    # print(t)
                    rs = [0] * (t + 1)
                    cs = [0] * (t + 1)
                    d1 = d2 = 0
                    for k in range(i,i+t+1):
                        rs[k - i] = rm[k][j+t] - (rm[k][j-1] if j > 0 else 0)
                    for k in range(j,j+t+1):
                        cs[k - j] = cm[i+t][k] - (cm[i-1][k] if i > 0 else 0)
                    for k in range(t+1):
                        d1 += grid[i+k][j+k]
                    for k in range(t+1):
                        d2 += grid[i+t-k][j+k]
                    # print(rs,cs,d1,d2)
                    if all(rs[i] - rs[i-1] == 0 for i in range(1,t+1)) and all(cs[i] - cs[i-1] == 0 for i in range(1,t+1)) and d1 == d2 == rs[0] == cs[0]:
                        res = max(res,t+1)
        return res