class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arr = sorted(list(set(x for x, _ in points)))
        res = 0
        for i in range(1,len(arr)):
            res = max(res, arr[i] - arr[i-1])
        return res