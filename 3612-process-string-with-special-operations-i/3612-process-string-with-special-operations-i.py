class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for i in s:
            if i == '*':
                if res:
                    res.pop()
            elif i == '#':
                res.extend(res)
            elif i == '%':
                res.reverse()
            else:
                res.append(i)
        return ''.join(res)