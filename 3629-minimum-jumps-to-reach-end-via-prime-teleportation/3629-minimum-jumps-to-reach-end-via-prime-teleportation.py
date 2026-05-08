class Solution:
    N = 10**6 + 5
    ps = [True] * N
    ps[0] = ps[1] = False
    for i in range(2, 1001):
        if ps[i]:
            for j in range(i * i, N, i):
                ps[j] = False
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        lim = nums[0]
        for c in nums:
            lim = max(lim, c)
        head = [-1] * (lim + 1)
        nxt = [-1] * n
        for i in range(n):
            val = nums[i]
            nxt[i] = head[val]
            head[val] = i
        dp = [-1] * n
        dp[0] = 0
        q = deque([0])
        seen = set()
        while q:
            dq = q.popleft()
            if dq == n - 1:
                return dp[dq]
            r = dq + 1
            if r < n and dp[r] == -1:
                dp[r] = dp[dq] + 1
                q.append(r)
            l = dq - 1
            if l >= 0 and dp[l] == -1:
                dp[l] = dp[dq] + 1
                q.append(l)
            val = nums[dq]
            if Solution.ps[val] and val not in seen:
                seen.add(val)
                for i in range(val, lim + 1, val):
                    j = head[i]
                    while j != -1:
                        if dp[j] == -1:
                            dp[j] = dp[dq] + 1
                            q.append(j)
                        j = nxt[j]
                    head[i] = -1
        return -1