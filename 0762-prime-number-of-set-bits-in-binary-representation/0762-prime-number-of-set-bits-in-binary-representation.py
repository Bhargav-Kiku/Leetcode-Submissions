class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res = 0
        for i in range(left, right+1):
            c = bin(i).count('1')
            if c in {2, 3, 5, 7, 11, 13, 17, 19}:
                res += 1
        return res