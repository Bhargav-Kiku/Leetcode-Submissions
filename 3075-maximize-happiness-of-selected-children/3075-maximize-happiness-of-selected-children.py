class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        res = 0
        t = 0
        for i in range(k):
            g = max(0, happiness[i] - i)
            if g <= 0:
                return res
            res += g
        return res