class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        n, m = len(boxGrid), len(boxGrid[0])
        mat = [['.'] * (n) for _ in range(m)]
        for i in range(n):
            l = m - 1
            j = n - i - 1
            k = m - 1
            while k >= 0:
                if boxGrid[j][k] == '#':
                    mat[l][i] = '#'
                    k -= 1
                    l -= 1
                elif boxGrid[j][k] == '*':
                    mat[k][i] = '*'
                    k -= 1
                    l = k
                else:
                    k -= 1
        return mat
