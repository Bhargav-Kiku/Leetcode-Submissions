import bisect
class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        def flatten(p):
            x, y = p
            if y == 0: return x
            if x == side: return side + y
            if y == side: return 3 * side - x
            return 4 * side - y
        arr = sorted(flatten(p) for p in points)
        n = len(arr)
        def midValid(d):
            for i in range(n):
                ptr = i
                cnt = 1
                while cnt < k:
                    tar = arr[ptr] + d
                    j = bisect.bisect_left(arr, tar)
                    if j == n:
                        break
                    ptr = j
                    cnt += 1
                    if d + arr[ptr] > arr[i] + 4 * side:
                        cnt = 0
                        break
                if cnt == k:
                    return False
            return True

        l, h = 0, side
        res = 0
        while l <= h:
            mid = (l + h) // 2
            if not midValid(mid):
                res = mid
                l = mid + 1
            else:
                h = mid - 1
        return res