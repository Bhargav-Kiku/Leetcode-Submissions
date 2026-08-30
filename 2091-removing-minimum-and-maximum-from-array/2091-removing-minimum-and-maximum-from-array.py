class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        i1 = i2 = 0
        n = len(nums)
        maxv = -float('inf')
        minv = float('inf')
        for i in range(n):
            if nums[i] < minv:
                minv = nums[i]
                i1 = i
            if nums[i] > maxv:
                maxv = nums[i]
                i2 = i
        print(i1, i2)
        return (min(max(i1, i2) + 1, n - min(i1, i2), min(i1, i2) + 1 + n - max(i1, i2)))