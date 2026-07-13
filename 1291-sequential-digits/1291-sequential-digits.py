class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        s = "123456789"
        l = str(low)
        h = str(high)
        for i in range(len(l), len(h) + 1):
            for st in range(0, 10 - i):
                num = int(s[st: st + i])
                if low <= num <= high:
                    res.append(num)
        return res