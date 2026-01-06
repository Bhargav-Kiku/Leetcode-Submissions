class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        f = Counter(nums)
        res = 0
        for i in nums:
            if i + k in f:
                res += f[i+k]
        return res