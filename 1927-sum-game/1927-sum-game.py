class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        s = 0
        lc = 0
        for i in range(n//2):
            if num[i] == '?':
                lc += 1
            else:
                s += int(num[i])

        for i in range(n//2, n):
            if num[i] == '?':
                lc -= 1
            else:
                s -= int(num[i])
        
        if lc == 0:
            if s == 0:
                return False
            return True
        elif lc % 2:
            return True
        return 2 * s != 9 * (-lc)