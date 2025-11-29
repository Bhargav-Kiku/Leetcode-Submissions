class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        o = sum((i & 1 == 1) for i in nums)
        # print(o)
        return [0]*(len(nums)-o) + [1]*(o)