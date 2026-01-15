class Solution:
    def findXY(self, arr):
        # print(arr)
        l = 1
        ml = 1
        for i in range(1,len(arr)):
            if arr[i-1] + 1 == arr[i]:
                l += 1
            else:
                l = 1
            if l > ml:
                ml = l
        # print(a,b)
        return ml

    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        h = self.findXY(sorted(hBars))
        v = self.findXY(sorted(vBars))
        return (min(h, v) + 1) ** 2