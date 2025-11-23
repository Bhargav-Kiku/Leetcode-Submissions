class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def dfs(i,j):
            if i < n and j < m and land[i][j] == 1:
                land[i][j] = 0
                x1, y1 = dfs(i+1,j)
                x2, y2 = dfs(i,j+1)
                return max(x1,x2,i),max(y1,y2,j)
            return 0,0

        n, m = len(land), len(land[0])
        res = []
        for i in range(n):
            for j in range(m):
                if land[i][j] == 1:
                    np = [i,j]
                    x,y = dfs(i,j)
                    np.append(x)
                    np.append(y)
                    res.append(np)
        return res