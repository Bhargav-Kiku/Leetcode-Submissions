class Solution(object):
    def solveSudoku(self,board):
        R=[set()for _ in range(9)]
        C=[set()for _ in range(9)]
        B=[set()for _ in range(9)]
        E=[]
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    E.append((r,c))
                else:
                    ch=board[r][c]
                    R[r].add(ch)
                    C[c].add(ch)
                    B[(r//3)*3+(c//3)].add(ch)
        def f(k):
            if k==len(E):
                return 1
            r,c=E[k]
            b=(r//3)*3+(c//3)
            for ch in"123456789":
                if ch not in R[r]and ch not in C[c]and ch not in B[b]:
                    board[r][c]=ch
                    R[r].add(ch)
                    C[c].add(ch)
                    B[b].add(ch)
                    if f(k+1):
                        return 1
                    board[r][c]="."
                    R[r].remove(ch)
                    C[c].remove(ch)
                    B[b].remove(ch)
            return 0
        f(0)