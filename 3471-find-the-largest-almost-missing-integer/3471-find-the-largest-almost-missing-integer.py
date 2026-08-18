class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == k:
            return max(nums)
        c = Counter(nums)
        if k == 1:
            for i, x in sorted(c.items(), reverse = True):
                if x == 1:
                    return i
        if c[nums[-1]] == 1 and c[nums[0]] == 1:
            return max(nums[0], nums[-1])
        if c[nums[0]] == 1:
            return nums[0]
        if c[nums[-1]] == 1:
            return nums[-1]
        return -1