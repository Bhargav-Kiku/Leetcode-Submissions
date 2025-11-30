class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 0: return 0
        f = Counter(nums)
        li = sorted(list(f.keys()))
        res = 0
        for i in li:
            n -= f[i]
            if n >= k:
                res += f[i]
            else:
                break
        return res