dirs = {(-1,-1),(-1,0),(-1,+1),(0,-1),(0,+1),(+1,-1),(+1,0),(+1,+1)}
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        n, m = len(board), len(board[0])
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        q = deque([(x,y)])
        while q:
            i, j = q.popleft()
            bomb = 0
            for x, y in dirs:
                if 0 <= i+x < n and 0 <= j+y < m:
                    # print(board[x][y])
                    if board[i+x][j+y] == 'M':
                        bomb += 1
            # print(i,j,bomb)
            if bomb == 0:
                if board[i][j] != 'E':
                    continue
                board[i][j] = 'B'
                for x, y in dirs:
                    if 0 <= i+x < n and 0 <= j+y < m:
                        q.append((i+x,j+y))
            else:
                board[i][j] = str(bomb)
        return board