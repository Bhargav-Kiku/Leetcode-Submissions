class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        for r in accounts:
            res = max(res, sum(r))
        return res