class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = max(costs) + 1
        cnt = [0] * (n)
        for i in costs:
            cnt[i] += 1
        res = 0
        for p, c in enumerate(cnt):
            if p > coins:
                break
            elif c > 0:
                res += min(c, coins//p)
                coins -= (c * p)
        return res