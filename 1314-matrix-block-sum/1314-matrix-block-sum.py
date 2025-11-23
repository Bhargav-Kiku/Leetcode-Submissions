class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for x in range(max(0,i-k),min(m-1,i+k)+1):
                    for y in range(max(0,j-k),min(n-1,j+k)+1):
                        ans[i][j] += mat[x][y]
        return ans