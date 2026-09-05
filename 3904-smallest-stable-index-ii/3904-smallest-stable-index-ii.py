class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        post = [0] * n
        post[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            post[i] = min(post[i+1], nums[i])
        ins = float('inf')
        cm = nums[0]
        for i in range(n):
            cm = max(nums[i], cm)
            if abs(cm - post[i]) <= k:
                return i
        return -1