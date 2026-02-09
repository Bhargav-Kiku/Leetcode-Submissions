class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        h = len(nums) - 1
        while l <= h:
            m = l + (h-l)//2
            if nums[m] == target:
                return True
            if nums[m] == nums[l]:
                l += 1
                continue
            if nums[m] >= nums[l]:
                if nums[m] > target >= nums[l]:
                    h = m-1
                else:
                    l = m+1
            else:
                if nums[m] < target <= nums[h]:
                    l = m+1
                else:
                    h = m-1
        return False