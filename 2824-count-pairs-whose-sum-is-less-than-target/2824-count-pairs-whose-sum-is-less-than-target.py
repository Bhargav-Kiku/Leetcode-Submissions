class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] < target:
                    res += 1
                else:
                    break
        return res