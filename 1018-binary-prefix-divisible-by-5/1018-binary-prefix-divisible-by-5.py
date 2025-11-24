class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = 0
        res = []
        for i in nums:
            n = (n * 2 + i) % 5
            if n == 0:
                res.append(True)
            else:
                res.append(False)
        return res