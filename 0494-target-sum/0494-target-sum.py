class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        @cache
        def back(c,idx):
            if idx == -1:
                if c == target:
                    return 1
                return 0
            return back(c-nums[idx],idx-1) + back(c+nums[idx],idx-1)
        return back(0,n)