class Solution:
    def maxTotalValue(self, nums, k):
        n = len(nums)
        Ob = ST(nums)
        pq = [(-Ob.query(i, n), i, n) for i in range(n)]
        res = 0
        for _ in range(k):
            val, l, r = pq[0]
            if val == 0:
                break
            res -= val
            heapq.heapreplace(pq, (-Ob.query(l, r - 1), l, r - 1))
        return res

class ST:
    def __init__(self, num):
        n = len(num)
        bw = n.bit_length()
        self.min = [[0] * n for _ in range(bw)]
        self.max = [[0] * n for _ in range(bw)]
        for i in range(n):
            self.min[0][i] = self.max[0][i] = num[i]
        for i in range(1, bw):
            for j in range(n - (1 << i) + 1):
                self.min[i][j] = min(self.min[i - 1][j], self.min[i - 1][j + (1 << (i - 1))])
                self.max[i][j] = max(self.max[i - 1][j], self.max[i - 1][j + (1 << (i - 1))])
    def query(self, l, r):
        k = (r - l).bit_length() - 1
        return max(self.max[k][l], self.max[k][r - (1 << k)]) - min(self.min[k][l], self.min[k][r - (1 << k)])