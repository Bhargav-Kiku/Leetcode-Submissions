MOD = 1000000007
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        res = 0
        maxq = deque()
        minq = deque()
        l = 0
        dp = [0] * (len(nums) + 2)
        dp[1] = 1
        for i, x in enumerate(nums):
            while maxq and x > maxq[-1]:
                maxq.pop()
            maxq.append(x)
            while minq and x < minq[-1]:
                minq.pop()
            minq.append(x)
            while maxq[0] - minq[0] > k:
                y = nums[l]
                if maxq[0] == y:
                    maxq.popleft()
                if minq[0] == y:
                    minq.popleft()
                l += 1
            res = (dp[i+1] - dp[l]) % MOD
            dp[i+2] = (dp[i+1] + res) % MOD
        return res