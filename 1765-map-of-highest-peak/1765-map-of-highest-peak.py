class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q = deque()
        n, m = len(isWater), len(isWater[0])
        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    q.append((i,j))
                    isWater[i][j] = 0
                else:
                    isWater[i][j] = -1
        t = n * m - len(q)
        while t:
            i, j = q.popleft()
            if i + 1 < n and isWater[i+1][j] == -1:
                t -= 1
                q.append((i+1,j))
                isWater[i+1][j] = isWater[i][j] + 1
            if j + 1 < m and isWater[i][j+1] == -1:
                t -= 1
                q.append((i,j+1))
                isWater[i][j+1] = isWater[i][j] + 1
            if i > 0 and isWater[i-1][j] == -1:
                t -= 1
                q.append((i-1,j))
                isWater[i-1][j] = isWater[i][j] + 1
            if j > 0 and isWater[i][j-1] == -1:
                t -= 1
                q.append((i,j-1))
                isWater[i][j-1] = isWater[i][j] + 1
        return isWater