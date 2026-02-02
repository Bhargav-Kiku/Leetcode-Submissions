class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        sl = SortedList(nums[1:1+dist])
        cs , ms = sum(sl[:k-2]), float('inf')
        for i in range(1+dist, n):
            if sl.bisect(nums[i]) <= k - 2:
                cs += nums[i]
            else:
                cs += sl[k-2]
            ms = min(ms, cs)
            sl.add(nums[i])
            if sl.bisect(nums[i - dist]) <= k - 2:
                cs -= nums[i - dist]
            else:
                cs -= sl[k - 2]
            sl.remove(nums[i - dist])
        return nums[0] + ms