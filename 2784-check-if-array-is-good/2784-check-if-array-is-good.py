class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        m = max(nums)
        c = [0] * (m + 1)
        for i in nums:
            c[i] += 1
            if i != m and c[i] > 1:
                return False
        for i in range(1, m):
            if c[i] != 1:
                return False
        return c[m] == 2