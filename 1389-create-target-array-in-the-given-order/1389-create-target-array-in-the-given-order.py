class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        n = len(index)
        for i in range(n):
            target.insert(index[i],nums[i])
        return target