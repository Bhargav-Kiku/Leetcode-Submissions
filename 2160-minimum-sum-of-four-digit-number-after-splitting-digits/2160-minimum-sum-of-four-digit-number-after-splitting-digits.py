class Solution:
    def minimumSum(self, num: int) -> int:
        s = []
        while num > 0:
            s.append(num % 10)
            num //= 10
        s.sort()
        return s[0] * 10 + s[1] * 10 + s[2] + s[3]