class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res = []
        g = []
        p = []
        for i in nums:
            if i < pivot:
                res.append(i)
            elif i > pivot:
                g.append(i)
            else:
                p.append(i)
        return res + p + g