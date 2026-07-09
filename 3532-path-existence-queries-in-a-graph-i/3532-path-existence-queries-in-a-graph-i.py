class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        g = [i for i in range(n)]
        l = 0
        for i in range(1, n):
            if nums[i] - nums[i-1] <= maxDiff:
                g[i] = l
            else: l = i
        res = []
        for i, j in queries:
            res.append(g[i] == g[j])
        return res