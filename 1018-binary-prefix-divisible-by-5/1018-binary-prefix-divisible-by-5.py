class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = 0
        res = []
        for i in nums:
            n = (n * 2 + i) % 5
            res.append(n==0)
        return res