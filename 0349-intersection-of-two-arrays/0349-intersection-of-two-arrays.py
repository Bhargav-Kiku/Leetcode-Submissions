class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        boo = [False] * (1001)
        for i in nums1:
            boo[i] = True
        res = []
        for i in nums2:
            if boo[i]:
                res.append(i)
                boo[i] = False
        return res