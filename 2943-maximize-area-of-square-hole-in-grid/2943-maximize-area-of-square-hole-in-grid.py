class Solution:
    def findXY(self, arr):
        # print(arr)
        a = arr[0]
        b = arr[0]
        c = arr[0]
        l = 1
        ml = 1
        for i in range(1,len(arr)):
            if arr[i-1] + 1 == arr[i]:
                l += 1
            else:
                l = 1
                c = arr[i]
            if l > ml:
                ml = l
                a = c
                b = arr[i]
        # print(a,b)
        return a, b

    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hx, hy = self.findXY(sorted(hBars))
        vx, vy = self.findXY(sorted(vBars))
        return (min(hy-hx, vy-vx) + 2) ** 2