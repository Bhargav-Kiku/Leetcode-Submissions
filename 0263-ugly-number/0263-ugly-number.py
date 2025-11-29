class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1 or n == 2:
            return True
        if n == 0:
            return False
        if n % 2 != 0:
            if n == 3:
                return True
            if n % 3 != 0:
                if n == 5:
                    return True
                if n % 5 != 0:
                    return False
                n /= 5
            else:
                n /= 3
        else:
            n /= 2
        return self.isUgly(n)