class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        pre = []
        xor = 0
        for i in arr:
            xor ^= i
            pre.append(xor)
        res = []
        for i, j in queries:
            res.append(pre[j] ^ (pre[i-1] if i > 0 else 0))
        return res