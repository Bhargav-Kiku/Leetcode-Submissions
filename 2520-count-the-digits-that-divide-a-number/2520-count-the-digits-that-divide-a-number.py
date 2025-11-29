class Solution:
    def countDigits(self, num: int) -> int:
        cn = num
        res = 0  
        while cn > 0:
            if num % (cn % 10) == 0:
                res += 1
            cn //= 10
        return res