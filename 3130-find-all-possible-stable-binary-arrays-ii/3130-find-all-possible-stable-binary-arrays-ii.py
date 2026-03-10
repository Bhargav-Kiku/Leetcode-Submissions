class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mo = (10**9)+7
        dp = [[[0,0] for _ in range(one+1)] for _ in range(zero+1)]
        for i in range(zero+1):
            dp[i][0] = [1,0] if i<=limit else [0,0]
        for j in range(one+1):
            dp[0][j] = [0,1] if j<=limit else [0,0]
        for i in range(1,zero+1):
            for j in range(1,one+1):
                dp[i][j]=[sum(dp[i-1][j]),sum(dp[i][j-1])]
                if i>limit:
                    dp[i][j][0]-=dp[i-limit-1][j][1]
                if j>limit:
                    dp[i][j][1]-=dp[i][j-limit-1][0]
                for t in range(2):
                    dp[i][j][t]%=mo
        return sum(dp[-1][-1])%mo