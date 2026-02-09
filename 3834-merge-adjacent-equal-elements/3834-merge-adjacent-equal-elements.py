class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        res = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            res.append(nums[i])
            while len(res) > 1 and res[-1] == res[-2]:
                res[-2] += res[-1]
                res.pop()
        return res