class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0
        def recur(i,c):
            if i == len(nums):
                self.res += c
                return
            recur(i+1,c^nums[i])
            recur(i+1,c)
        recur(0,0)
        return self.res