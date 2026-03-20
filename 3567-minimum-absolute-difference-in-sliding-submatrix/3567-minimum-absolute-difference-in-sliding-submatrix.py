class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0 for _ in range(n-k+1)] for _ in range(m-k+1)]
        for i in range(m-k+1):
            for j in range(n-k+1):
                val = []
                for z in range(i,i+k):
                    for x in range(j,j+k):
                        val.append(grid[z][x])
                val.sort()
                m = float('inf')
                for q in range(1,len(val)):
                    if val[q] != val[q-1]:
                        m = min(m,val[q]-val[q-1])
                ans[i][j] = m if m != float('inf') else 0
        return ans