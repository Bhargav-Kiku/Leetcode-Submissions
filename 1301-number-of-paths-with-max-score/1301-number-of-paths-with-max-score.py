class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10 ** 9 + 7
        n = len(board)
        dp = [[-1] * n for _ in range(n)]
        ws = [[0] * n for _ in range(n)]
        dp[-1][-1] = 0
        ws[-1][-1] = 1
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X' or (i == n - 1 and j == n - 1):
                    continue
                res = -1
                c = 0
                for x, y in ((i + 1, j), (i, j + 1), (i + 1, j + 1)):
                    if x >= n or y >= n or dp[x][y] == -1:
                        continue
                    if dp[x][y] > res:
                        res = dp[x][y]
                        c = ws[x][y]
                    elif dp[x][y] == res:
                        c = (c + ws[x][y]) % MOD
                if res == -1:
                    continue
                val = int(board[i][j]) if board[i][j].isdigit() else 0
                dp[i][j] = res + val
                ws[i][j] = c
        if dp[0][0] == -1:
            return [0, 0]
        return [dp[0][0], ws[0][0]]