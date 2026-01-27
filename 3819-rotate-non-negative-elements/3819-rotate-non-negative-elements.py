class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        ge = []
        for i in nums:
            if i >= 0:
                ge.append(i)
        n = len(nums)
        m = len(ge)
        j = 0
        for i in range(n):
            if nums[i] >= 0:
                nums[i] = ge[(j + k) % m]
                j += 1
        return nums