class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        res = 0
        f = True
        for i in range(len(nums)):
            if (i + 1) % 6 == 0:
                f = not f
            if nums[i] & 1:
                f = not f
            res += (nums[i] * (1 if f else -1))
        return res