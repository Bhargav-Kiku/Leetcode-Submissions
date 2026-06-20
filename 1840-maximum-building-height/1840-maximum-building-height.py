class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        if not restrictions:
            return n - 1
        restrictions.append([1, 0])
        restrictions.sort()
        for i in range(1, len(restrictions)):
            d = restrictions[i][0] - restrictions[i - 1][0]
            restrictions[i][1] = min(restrictions[i][1],restrictions[i - 1][1] + d)
        for i in range(len(restrictions) - 2, -1, -1):
            d = restrictions[i + 1][0] - restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1],restrictions[i + 1][1] + d)
        maxm = 0
        for i in range(1, len(restrictions)):
            x1, h1 = restrictions[i - 1]
            x2, h2 = restrictions[i]
            d = x2 - x1
            maxm = max(maxm, (h1 + h2 + d) // 2)
        x, h = restrictions[-1]
        maxm = max(maxm, h + (n - x))
        return maxm