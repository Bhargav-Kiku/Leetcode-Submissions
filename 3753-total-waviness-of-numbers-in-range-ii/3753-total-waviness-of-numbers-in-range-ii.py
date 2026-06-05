class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        wavy = [l*100+m*10+r for l,m,r in product(range(10),range(10),range(10)) if l < m > r or l > m < r]
        ix = bisect_left(wavy,100)
        def waves(n):
            res, suf, pow = 0, 0, 1
            while n >= 100:
                pre, win = n//1000, n%1000
                x = bisect_left(wavy, win)
                eq = x < len(wavy) and wavy[x] == win
                n1 = min(x, ix)
                n0 = max(0, x-ix)
                nge1 = max(0, ix-x)
                nge0 = min(len(wavy)-x, len(wavy)-ix)
                res += (n1*pre + n0*(pre+1) + nge0*pre + nge1*max(0,pre-1))*pow + eq*(suf+1)
                suf += n%10 *pow
                n //= 10; pow *= 10
            return res
        return waves(num2) - waves(num1-1)
        