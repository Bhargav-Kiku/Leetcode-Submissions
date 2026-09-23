class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        tot = sum(nums)
        if tot < x:
            return -1
        n = len(nums)
        if tot == x:
            return n
        target = tot - x
        res = 0
        i = 0
        cur = 0
        for j in range(n):
            cur += nums[j]
            while cur > target:
                cur -= nums[i]
                i += 1
            if cur == target:
                res = max(res, j - i + 1)
        if res == 0:
            return -1
        return n - res