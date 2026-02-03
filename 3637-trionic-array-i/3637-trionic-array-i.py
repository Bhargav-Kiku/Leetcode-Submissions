class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        p1 = False
        p2 = False
        p3 = False
        i = 1
        while i < n:
            if nums[i] - nums[i-1] > 0:
                i += 1
            else:
                p1 = True
                break
        if i == 1:
            return False
        # print(i, p1)
        while i < n:
            if nums[i] - nums[i-1] < 0:
                i += 1
            else:
                p2 = True
                break
        # print(i, p2)
        while i < n:
            if nums[i] - nums[i-1] > 0:
                i += 1
            else:
                p3 = True
                break
        # print(i, p3)
        return p2 and not p3 and i == n