class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        for i in range(n):
            for j in range(1,nums[i]):
                if (j | j+1) == nums[i]:
                    res[i] = j
                    break
        return res