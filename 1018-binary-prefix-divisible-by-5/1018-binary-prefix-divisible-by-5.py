class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = 0
        res = []
        for i in nums:
            n <<= 1
            n |= i
            if n % 5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res