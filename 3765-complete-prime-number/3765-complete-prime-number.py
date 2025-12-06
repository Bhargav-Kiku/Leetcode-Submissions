class Solution:
    def completePrime(self, num: int) -> bool:
        def isPrime(x):
            if x == 1:
                return False
            if x == 2 or x == 3:
                return True
            for i in range(2,int(x**(0.5)) + 1):
                if x % i == 0:
                    return False
            return True
        x = 0
        tn = 10
        while tn <= num:
            x = num % tn
            tn *= 10
            if not isPrime(x):
                return False
        x = 0
        tn = 10**len(str(num))
        while tn > 0:
            x = num // tn
            tn //= 10
            if not isPrime(x):
                return False
        return True