MOD = 1000000007
class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        cnt = [0] * 30
        for i in nums:
            for j in range(30):
                if i >> j & 1:
                    cnt[j] += 1
        res = 0
        for i in range(k):
            t = 0
            for j in range(30):
                if cnt[j] > i:
                    t |= (1 << j)
            res = (res + t * t) % MOD
        return res