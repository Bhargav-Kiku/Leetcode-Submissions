class Solution:
    def i_s(self, nums):
        n = len(nums)
        for i in range(1,n):
            if nums[i] < nums[i-1]:
                return False
        return True
    def minimumPairRemoval(self, nums: List[int]) -> int:
        res = 0
        while not self.i_s(nums):
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