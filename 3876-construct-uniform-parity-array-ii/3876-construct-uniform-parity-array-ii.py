class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        oddp = False
        minOdd = -1
        for i in nums1:
            if i % 2:
                if oddp:
                    minOdd = min(minOdd, i)
                else:
                    minOdd = i
                    oddp = True
        if not oddp: return True
        return min(nums1) == minOdd
