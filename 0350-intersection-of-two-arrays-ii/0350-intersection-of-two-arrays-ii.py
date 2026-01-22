class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        c = Counter(nums1)
        for j in nums2:
            if c[j] > 0:
                c[j] -= 1
                res.append(j)
        return res