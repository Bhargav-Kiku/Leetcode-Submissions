class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        f = Counter(nums)
        li = sorted(list(f.keys()))
        n = len(nums)
        res = 0
        for i in li:
            n -= f[i]
            if n >= k:
                res += f[i]
            else:
                break
        return res