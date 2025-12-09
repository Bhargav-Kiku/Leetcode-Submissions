MOD = 1000000007
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        f = Counter(nums)
        mp = defaultdict(int)
        mp[nums[0]] += 1
        f[nums[0]] -= 1
        n = len(nums)
        res = 0
        for i in range(1,n-1):
            # print(mp,f)
            f[nums[i]] -= 1
            v = nums[i] * 2
            if v in mp:
                res = (res + (mp[v] * f[v])) % MOD
            mp[nums[i]] += 1
            # print(res)
        return res