class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False
        buck = {}
        w = valueDiff + 1
        for i, num in enumerate(nums):
            n = num // w
            if n in buck:
                return True
            if n-1 in buck and num-buck[n-1] <= valueDiff:
                return True
            if n+1 in buck and buck[n+1] - num <= valueDiff:
                return True
            buck[n] = num
            if i >= indexDiff:
                del buck[nums[i-indexDiff]//w]
        return False