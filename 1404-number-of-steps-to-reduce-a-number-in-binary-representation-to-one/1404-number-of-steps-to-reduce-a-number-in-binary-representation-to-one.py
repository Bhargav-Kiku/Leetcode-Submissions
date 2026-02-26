class Solution:
    def numSteps(self, s: str) -> int:
        res = 0
        n = len(s)
        s = list(s)
        i = n - 1
        while i > 0:
            if s[i] == '0':
                res += 1
                i -= 1
            else:
                while i > 0 and s[i-1] != '0':
                    res += 1
                    i -= 1
                if i != 0:
                    res += 2
                    s[i - 1] = '1'
                    i -= 1
                else:
                    return res + 2
            # print(i, res)
        return res