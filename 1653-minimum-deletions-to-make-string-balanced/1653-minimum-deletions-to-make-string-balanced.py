class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        pre = [0] * (n + 1)
        suf = [0] * (n + 1)
        for i in range(1,n + 1):
            if s[i - 1] == 'b':
                pre[i] = pre[i-1] + 1
            else:
                pre[i] = pre[i-1]
        for i in range(n - 1, -1, -1):
            if s[i] == 'a':
                suf[i] = suf[i+1] + 1
            else:
                suf[i] = suf[i+1]
        res = n
        # print(*pre)
        # print(*suf)
        for i in range(n+1):
            res = min(res, pre[i] + suf[i])
        return res