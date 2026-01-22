class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        res = 0
        while nums != sorted(nums):
            mins = float('inf')
            idx = 0
            for i in range(len(nums)-1):
                if (nums[i] + nums[i+1]) < mins:
                    mins = nums[i] + nums[i+1]
                    idx = i
            nums = nums[:idx] + [nums[idx] + nums[idx+1]] + nums[idx+2:]
            # print(nums)
            res += 1
        return res