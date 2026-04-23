class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        mp = defaultdict(list)
        for i, v in enumerate(nums):
            mp[v].append(i)
        for pos in mp.values():
            tot = sum(pos)
            ls = 0
            m = len(pos)
            for i in range(m):
                rs = tot - ls - pos[i]
                l = pos[i] * i - ls
                r = rs - pos[i] * (m - i - 1)
                res[pos[i]] = l + r
                ls += pos[i]
        return res