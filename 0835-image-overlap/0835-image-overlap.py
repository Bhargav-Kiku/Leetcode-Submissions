import numpy as np
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        A = np.array(A)
        B = np.array(B)
        dim = len(A)
        bp = np.pad(B, dim-1, mode='constant', constant_values=(0, 0))
        maxo = 0
        for x_shift in range(dim*2 - 1):
            for y_shift in range(dim* 2 - 1):
                kernel = bp[x_shift:x_shift+dim, y_shift:y_shift+dim]
                nz = np.sum(A * kernel)
                maxo = max(maxo, nz)
        return int(maxo)