class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = sum(nums)
        if s % p == 0: return 0
        n = len(nums)
        res = n
        for i in range(n):
            t = 0
            for j in range(i,n):
                t += nums[j]
                if (s - t) % p == 0:
                    res = min(res,j-i+1)
        if res == n: return -1
        return res