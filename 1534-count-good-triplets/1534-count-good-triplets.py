class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0
        n = len(arr)
        for i in range(n):
            x = arr[i]
            for j in range(i+1,n):
                y = arr[j]
                if abs(x - y) > a: continue
                for k in range(j+1, n):
                    z = arr[k]
                    if abs(x - z) <= c and abs(y - z) <= b:
                        res += 1
        return res