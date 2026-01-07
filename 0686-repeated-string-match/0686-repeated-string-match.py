class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        j = 0
        def check(j):
            res = 1
            while j < len(b):
                if b[j:j+len(a)] == a:
                    res += 1
                    j += len(a)
                else:
                    if b[j:] == a[:len(b[j:])]:
                        res += 1
                        j += len(b[j:])
                    else:
                        return -1
            return res
        for i in range(len(a)):
            if a[i:i+len(b)] == b[:len(a)-i]:
                res = check(len(a[i:]))
                if res != -1:
                    return res
        return -1