class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(1, n):
            if nums[i] > nums[i-1] + 1:
                for j in range(nums[i-1] + 1, nums[i]):
                    res.append(j)
        return res