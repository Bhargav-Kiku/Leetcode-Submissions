class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        n = len(candies)
        res = [False] * n
        for i in range(n):
            res[i] = ((candies[i] + extraCandies) >= m)
        return res