class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        sn = len(set(nums))
        wm = {}
        res = 0
        i = 0
        j = 0
        while j < n:
            if nums[j] not in wm:
                wm[nums[j]] = 0
            wm[nums[j]] += 1
            while len(wm) == sn:
                wm[nums[i]] -= 1
                if wm[nums[i]] == 0:
                    del wm[nums[i]]
                i += 1
            res += i
            j += 1
        return res