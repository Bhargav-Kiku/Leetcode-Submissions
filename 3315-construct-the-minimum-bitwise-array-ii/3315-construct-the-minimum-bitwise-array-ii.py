class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        for i in range(n):
            if nums[i] % 2 == 0:
                res[i] = -1
            else:
                c = -1
                while nums[i] & 1 == 1:
                    c += 1
                    nums[i] >>= 1
                # print(i, c, nums[i] << 1, (1 << c) - 1)
                res[i] = (nums[i] << (c + 1)) | ((1 << c) - 1)
        return res