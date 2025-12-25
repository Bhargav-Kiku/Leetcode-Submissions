class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        n = len(happiness)
        happiness.sort(reverse = True)
        res = 0
        t = 0
        for i in range(n):
            res += max(0, happiness[i] - t)
            if t < k - 1:
                t += 1
            else:
                return res