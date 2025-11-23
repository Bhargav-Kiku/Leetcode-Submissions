class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [1 if x & 1 else 0 for x in nums]
        pre = [0]
        for i in nums:
            pre.append(pre[-1]+i)
        i = 0
        j = 0
        n = len(nums)
        f = Counter(pre)
        res = 0
        for i, j in f.items():
            if i - k in f:
                res += (j * f[i-k])
        return res