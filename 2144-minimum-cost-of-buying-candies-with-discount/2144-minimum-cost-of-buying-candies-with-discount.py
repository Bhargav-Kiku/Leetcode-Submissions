class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        na = sorted(cost, reverse = True)
        res = 0
        for i in range(0, len(cost), 3):
            res += sum(na[i:i+2])
        return res