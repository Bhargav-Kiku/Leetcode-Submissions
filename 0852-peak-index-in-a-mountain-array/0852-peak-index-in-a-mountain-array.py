class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 1
        h = len(arr) - 2
        while l <= h:
            m = l + (h - l) // 2
            if (arr[m] > arr[m-1] and arr[m] > arr[m+1]):
                return m
            elif arr[m] > arr[m-1]:
                l = m + 1
            else:
                h = m - 1