class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = []
        for i in str(n):
            if i != '0':
                x.append(i)
        if not x: return 0
        return sum(int(k) for k in x) * int(''.join(x))