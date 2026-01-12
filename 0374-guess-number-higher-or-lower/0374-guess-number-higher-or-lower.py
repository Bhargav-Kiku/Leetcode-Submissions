# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        h = n
        while l <= h:
            m = l + (h - l) // 2
            print(l,h,m)
            v = guess(m)
            # print(v)
            if v == 0:
                return m
            elif v < 0:
                h = m - 1
            else:
                l = m + 1
        