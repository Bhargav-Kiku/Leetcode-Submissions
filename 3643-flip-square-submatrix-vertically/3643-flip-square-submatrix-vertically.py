class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        i = x
        j = x + k - 1
        while i < j:
            for a in range(y, y + k):
                grid[i][a], grid[j][a] = grid[j][a], grid[i][a]
            i += 1
            j -= 1
        return grid