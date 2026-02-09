class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        res = []
        xor = 0
        for i in nums:
            xor ^= i
        n = len(nums)
        k = (1 << maximumBit) - 1
        for i in range(n-1,-1,-1):
            res.append(k^xor)
            xor ^= nums[i]
        return res