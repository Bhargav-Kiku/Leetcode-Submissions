class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: (x[1]))
        n = len(pairs)
        res = 1
        l = pairs[0][1]
        for i in range(1,n):
            if (l < pairs[i][0]):
                res += 1
                l = pairs[i][1]
        return res