class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(33):
            bs = 0
            for n in nums:
                # if n < 0:
                #     n = n & (2**32-1)
                bs += (n >> i) & 1
            bs %= 3
            res |= bs << i
        if res >= 2 ** 31:
            res -= 2**32
        return res