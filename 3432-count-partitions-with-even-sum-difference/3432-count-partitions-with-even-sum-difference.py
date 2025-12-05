class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        s = nums[0]
        t = sum(nums)
        n = len(nums)
        res = 0
        for i in range(1,n):
            if abs(t-s-s) & 1 == 0:
                res += 1
            s += nums[i]
            # print(s)
        return res