class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 1
        w = {nums[0]:1}
        s = 0
        n = len(nums)
        for i in range(1,n):
            w[nums[i]] = w.get(nums[i],0) + 1
            # print(i,w)
            while w[nums[i]] > k:
                # print("Here")
                w[nums[s]] -= 1
                s += 1
            res = max(res,i-s+1)
            # print(res)
        return res