m = 1000000007
class Solution:
    def maxNiceDivisors(self, n: int) -> int:
        if n <= 3:
            return n
        if n % 3 == 0:
            return pow(3,n//3,m)
        if n % 3 == 1:
            return (pow(3,(n-4)//3,m) * 4) % m
        return (2 * pow(3, n//3, m)) % m