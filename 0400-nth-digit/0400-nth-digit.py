class Solution(object):
    def findNthDigit(self, n):
        i = 1
        c = 9
        s = 1

        while n > i * c:
            n -= i * c
            i += 1
            c *= 10
            s *= 10

        num = s + (n - 1) // i
        return int(str(num)[(n - 1) % i])