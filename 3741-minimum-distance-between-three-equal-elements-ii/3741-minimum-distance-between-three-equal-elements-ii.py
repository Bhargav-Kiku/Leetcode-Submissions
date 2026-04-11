class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        res = float('inf')
        f = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in f:
                f[nums[i]] = deque()
            f[nums[i]].append(i)
            if len(f[nums[i]]) == 3:
                v =  f[nums[i]][2] - f[nums[i]].popleft()
                if v * 2 < res:
                    res = v * 2
        return -1 if res == float('inf') else res