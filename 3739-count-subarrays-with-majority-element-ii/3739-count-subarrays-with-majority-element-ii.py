class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pref = n
        freq = [0] * (2 * n + 1)
        freq[n] = 1
        l = 0
        res = 0
        for x in nums:
            if x == target:
                l += freq[pref]
                pref += 1
            else:
                pref -= 1
                l -= freq[pref]
            freq[pref] += 1
            res += l
        return res