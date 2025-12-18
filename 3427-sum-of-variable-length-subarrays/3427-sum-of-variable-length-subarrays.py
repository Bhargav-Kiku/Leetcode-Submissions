class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        pre = [0]
        for i in nums:
            pre.append(pre[-1] + i)
        res = 0
        for i in range(len(nums)):
            res += (pre[i+1] - pre[max(0, i - nums[i])])
        return res