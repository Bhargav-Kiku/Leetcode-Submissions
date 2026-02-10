class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        vis = set()
        for i in range(n):
            vis.clear()
            bal = 0
            if res > n - i: break
            for j in range(i,n):
                if nums[j] not in vis:
                    if nums[j] & 1: bal += 1
                    else: bal -= 1
                    vis.add(nums[j])
                if bal == 0:
                    res = max(res, j - i + 1)
        return res