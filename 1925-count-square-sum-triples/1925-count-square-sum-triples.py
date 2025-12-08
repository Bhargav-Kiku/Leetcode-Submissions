class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        sq = [x**2 for x in range(0,n+1)]
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                for k in range(j+1,n+1):
                    if sq[i] + sq[j] == sq[k]:
                        res += 1
        return res * 2