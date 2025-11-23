class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        vals = []
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                vals.append(grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] + grid[i][j] + grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1])
        return max(vals)