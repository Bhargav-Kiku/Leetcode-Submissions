class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = nums[:]
        for i in range(1,len(nums),2):
            res[i], res[i-1] = res[i-1], res[i]
        return res