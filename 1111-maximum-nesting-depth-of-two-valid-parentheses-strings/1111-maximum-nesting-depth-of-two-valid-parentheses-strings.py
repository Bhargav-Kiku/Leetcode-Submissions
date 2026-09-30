class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        a = 0
        b = 0
        n = len(seq)
        res = [0] * n
        for i in range(n):
            if seq[i] == '(':
                if a > b:
                    b += 1
                    res[i] = 1
                else:
                    a += 1
                    res[i] = 0
            else:
                if a > b:
                    a -= 1
                    res[i] = 0
                else:
                    b -= 1
                    res[i] = 1
        return res
