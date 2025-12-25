class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        n = len(happiness)
        happiness.sort(reverse = True)
        # res = happiness[0]
        res = 0
        t = 0
        for i in range(n):
            res += max(0, happiness[i] - t)
            if t < k:
                t += 1
            if t == k:
                break
        return res