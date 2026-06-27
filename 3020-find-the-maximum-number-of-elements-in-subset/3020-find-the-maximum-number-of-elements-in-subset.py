class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        res = 1
        c = Counter(nums)
        mapy = defaultdict(int)
        for i, x in sorted(c.items(), reverse = True):
            if x == 1:
                mapy[i] = max(mapy[i], 1)
            else:
                mapy[i] = mapy[i**(2)] + 1
            res = max(res, mapy[i] * 2 - 1)
            # print(i, res)
        # print(mapy)
        return max(res, c[1] if c[1] % 2 == 1 else c[1] - 1)