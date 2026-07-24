class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        print(n)
        pre = set()
        for i in range(n):
            for j in range(i + 1, n):
                pre.add(nums[i] ^ nums[j])
        pre.add(0)
        res = set()
        for i in range(n):
            for x in pre:
                res.add(nums[i] ^ x)
        return len(res)