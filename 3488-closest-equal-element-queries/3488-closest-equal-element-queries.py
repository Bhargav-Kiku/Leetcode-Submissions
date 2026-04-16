class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        f = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in f:
                f[nums[i]] = []
            f[nums[i]].append(i)
        res = []
        for q in queries:
            v = nums[q]
            if len(f[v]) == 1:
                res.append(-1)
            else:
                l = bisect.bisect_left(f[v],q)
                if f[v][l] == q:
                    l = l - 1
                m = len(f[v])
                r = (l + 2) % (m)
                l = (l % m)
                r, l = f[v][r], f[v][l]
                ans = float('inf')
                # print(l,q,r)
                if l < q:
                    ans = q - l
                else:
                    ans = q + n - l
                # print(ans)
                if r > q:
                    ans = min(ans, r - q)
                else:
                    ans = min(ans, n + r - q)
                # print(ans)
                res.append(ans)
        return res