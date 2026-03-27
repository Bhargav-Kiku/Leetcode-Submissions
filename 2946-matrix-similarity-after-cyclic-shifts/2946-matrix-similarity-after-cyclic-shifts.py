class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat)
        k = k % len(mat[0])
        for i in range(n):
            r = mat[i]
            if i & 1:
                nr = r[-k:] + r[:-k]
            else:
                nr = r[k:] + r[:k]
            if r != nr:
                return False
            # print(nr)
        return True