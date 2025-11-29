class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ''
        n = len(num1) - 1
        m = len(num2) - 1
        c = 0
        while n >= 0 and m >= 0:
            v = int(num1[n]) + int(num2[m]) + c
            res = res + str(v % 10)
            c = v // 10
            n -= 1
            m -= 1
        if n >= 0:
            v = int(num1[n]) + c
            res = res + str(v % 10)
            c = v // 10
            n -= 1
        if m >= 0:
            v = int(num2[m]) + c
            res = res + str(v % 10)
            c = v // 10
            m -= 1
        if c:
            res = res + str(c)
        return res[::-1]