class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        vis = set()
        for i in nums:
            if i in vis:
                return i
            vis.add(i)