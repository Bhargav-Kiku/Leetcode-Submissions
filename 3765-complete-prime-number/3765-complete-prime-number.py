p = {}
class Solution:
    def isPrime(self, x):
        if x in p:
            return p[x]
        if x == 1:
            return False
        for i in range(2,int(x**(0.5)) + 1):
            if x % i == 0:
                p[x] = False
                return False
        p[x] = True
        return True
    def completePrime(self, num: int) -> bool:
        x = 0
        tn = 10
        while tn <= num:
            x = num % tn
            tn *= 10
            if not self.isPrime(x):
                return False
        x = 0
        tn = 10**len(str(num))
        while tn > 0:
            x = num // tn
            tn //= 10
            if not self.isPrime(x):
                return False
        return True