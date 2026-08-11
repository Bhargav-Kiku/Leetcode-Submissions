class Solution:
    def missingInteger(self, A: list[int]) -> int:
        n = len(A)
        vis = set(A)
        tot = A[0]
        for i in range(1, n):
            if A[i] == A[i - 1] + 1:
                tot += A[i]
            else:
                break
        while tot in vis:
            tot += 1
        return tot