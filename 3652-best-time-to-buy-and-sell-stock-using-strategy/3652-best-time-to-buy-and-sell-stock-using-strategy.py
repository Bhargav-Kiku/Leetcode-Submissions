class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        pros = [0] * (n + 1)
        pris = [0] * (n + 1)
        for i in range(n):
            pros[i + 1] = pros[i] + prices[i] * strategy[i]
            pris[i + 1] = pris[i] + prices[i]
        res = pros[n]
        for i in range(k - 1, n):
            lp = pros[i - k + 1]
            rp = pros[n] - pros[i + 1]
            cp = pris[i + 1] - pris[i - k // 2 + 1]
            res = max(res, lp + cp + rp)
        return res