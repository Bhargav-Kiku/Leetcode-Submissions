class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        res = 0
        for i in range(num1,num2+1):
            s = str(i)
            n = len(s)
            for k in range(1,n-1):
                if (s[k-1] < s[k] > s[k+1] or s[k-1] > s[k] < s[k+1]):
                    res += 1
        return res