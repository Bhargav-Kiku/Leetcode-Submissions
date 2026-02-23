class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False
        t = []
        res = [False] * (1 << k)
        for i in range(k):
            t.append(s[i])
        res[int(''.join(t),2)] = True
        for i in range(k, n):
            t.pop(0)
            t.append(s[i])            
            res[int(''.join(t),2)] = True
        return all(res)