class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: (x[1], -x[0]))
        # print(pairs)
        n = len(pairs)
        dp = [0] * n
        for i in range(n):
            c, d = pairs[i]
            for j in range(i-1, -1, -1):
                a, b = pairs[j]
                if b < c:
                    dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] == 0:
                dp[i] = 1
            # print(dp)
        return max(dp)