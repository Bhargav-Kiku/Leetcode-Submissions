class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        ca = [0] * 3
        for i in stones:
            ca[i % 3] += 1
        if ca[0] % 2 == 0:
            return min(ca[1], ca[2]) >= 1
        return abs(ca[1] - ca[2]) >= 3