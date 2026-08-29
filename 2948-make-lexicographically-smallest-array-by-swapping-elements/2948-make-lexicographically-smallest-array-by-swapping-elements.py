class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        arr = sorted((v, i) for i, v in enumerate(nums))
        i = 0
        while i < len(nums):
            j = i + 1            
            while j < len(nums) and arr[j][0] - arr[j - 1][0] <= limit:
                j += 1
            x = sorted(x[1] for x in arr[i:j])
            for k in range(len(x)):
                nums[x[k]] = arr[i + k][0]
            i = j
        return nums