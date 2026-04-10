class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        res = float('inf')
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] != nums[j]: continue
                for k in range(j+1,n):
                    if nums[i] != nums[k]: continue
                    if (k - i) * 2 < res:
                        res = (k - i) * 2
        if res == float('inf'): return -1
        return res