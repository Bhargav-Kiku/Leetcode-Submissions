class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        l = len(strs[0])
        n = len(strs)
        res = 0
        for i in range(l):
            for j in range(1,n):
                if strs[j-1][i] > strs[j][i]:
                    res += 1
                    # print(i,j)
                    break
        return res