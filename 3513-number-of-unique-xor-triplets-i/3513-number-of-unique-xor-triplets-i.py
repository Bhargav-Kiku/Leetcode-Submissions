class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        msb = n.bit_length()
        return pow(2,msb) # can generate all numbers = [0, 2^(msb+1) - 1]