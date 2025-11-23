class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        e = nums[0]
        c = 1
        for i in nums:
            if e == i:
                c += 1
            elif c == 0:
                e = i
                c = 1
            else:
                c -= 1
        c = nums.count(e)
        nc = 0
        n = len(nums)
        for i in range(n-1):
            if nums[i] == e:
                nc += 1
            if nc > (i+1)//2 and (c-nc) > (n-i-1)//2:
                return i
        return -1